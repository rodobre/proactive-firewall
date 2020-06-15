from RedisQueue import RedisQueue
from anomaly_detection import AnomalyDetection
from model import load_model, dump_model, load_labels
import classifier
import json
import numpy as np
import threading
import os
from database_conn import *

# minimum confidence threshold for the program
CONFIDENCE_THRESHOLD = 0.71

# instantiate a database connection
db_conn = init_connection(os.getenv('MYSQL_PASSWORD'), os.getenv('MYSQL_USER'))

if __name__ == '__main__':

    # load the classifiying model
    clf_model = load_model('clf_model')

    # load the labels
    labels = load_labels('clf_labels')
    
    # debug printing, used for verification
    print(clf_model)
    print(labels)
    print(len(clf_model), len(labels))

    # train the SVM model with the fetched information
    print(f'Training the SVM model...')
    clf = classifier.fit_model(clf_model, labels)

    # print the accuracy, precision and recall
    print(f'Accuracy: {clf[1]}\nPrecision: {clf[2]}\nRecall: {clf[3]}')
    print(f'Finished training the SVM model..')
    clf = clf[0]

    # create the anomaly detection instance
    print('Instantiating anomaly detection algorithm...')
    anomaly_detection = AnomalyDetection()
    anomaly_detection.load_model('anomaly_detection.csv')
    anomaly_detection.train_forest()
    print('Finished instantiating anomaly detection algorithm')

    # initialize the forwards-backwards pipelines
    print('Initializing pipelines...')
    redis_packet_queue = RedisQueue('packet_worker_queue')
    redis_results_queue = RedisQueue('packet_results_queue')
    print('Pipelines initialized, awaiting messages...')

    while True:
        # fetch a packet
        recv_info = redis_packet_queue.get()

        if not recv_info:
            continue

        # load the packet as a JSON object and decode the features
        parsed_json = json.loads(recv_info)
        json_decoded_packet = parsed_json['packet']
        json_decoded_packid = parsed_json['id']
        json_decoded_src    = parsed_json['src']
        json_decoded_dst    = parsed_json['dst']


        # perform isolation, observe if outlier
        result = anomaly_detection.predict_data(json_decoded_packet)

        if isinstance(result, list):
            result = result[0]
        
        if result == 1:
            continue
        
        # We are dealing with an outlier
        prediction = classifier.predict(clf, json_decoded_packet)
        best_conf = max(prediction[2][0])

        # decide if the finding is significant
        if best_conf > CONFIDENCE_THRESHOLD:
            print(f'Labeled packet {json_decoded_packet} with id {json_decoded_packid} as {prediction[1]} with confidence {best_conf}')
            execute_prepared_update(db_conn, 'INSERT INTO THREATS (date, prediction_type, src, dst, confidence) VALUES (NOW(), %s, %s, %s, %s);', \
                                (prediction[1], json_decoded_src, json_decoded_dst, float(best_conf)))
        else:
            print(f'Labeled packet {json_decoded_packet} with id {json_decoded_packid} as FALSE POSITIVE due to confidence < {CONFIDENCE_THRESHOLD} [{best_conf}]')

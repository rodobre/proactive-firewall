import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split

label_encoding = {
    0: 'File scan / Crawling',
    1: 'Binary/Encrypted traffic',
    2: 'Denial of service'
}

# Function needed for model fitting
# Instantiates a pipeline which performs standard scaling...
# ... to reduce standard deviation of the dataset to 1
def fit_model(model, labels):
    model_np  = np.array(model)
    labels_np = np.array(labels)

    # Train test split in order to determine model accuracy
    X_train, X_test, y_train, y_test = train_test_split(
        model_np, labels_np, test_size=0.2, random_state=42)
    
    print('Training length:', len(X_train))
    print('Test length: ', len(X_test))

    # Instantiate the pipeline
    clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))

    # Fit the model
    clf.fit(X_train, y_train)

    # Get the prediction on the test dataset
    y_pred = clf.predict(X_test)

    # Get the metrics of our model
    acc, prec, rec = metrics.accuracy_score(y_test, y_pred),                        \
        metrics.precision_score(y_test, y_pred, average='micro'), metrics.recall_score(y_test, y_pred, average='micro')
    
    # Refit on the entire dataset
    clf = make_pipeline(StandardScaler(),   \
        SVC(gamma='auto', probability=True))
    clf.fit(model_np, labels_np)

    # Return the classifier with the metrics
    return (clf, acc, prec, rec)


# Return the prediction for a given query
def predict(clf, query):
    # Instantiate the query numpy array
    query_np = np.array(query)

    # Calculate the confidence of the classifier
    confidence = clf.predict_proba(query_np)

    # Label the prediction
    prediction = np.argmax(confidence)

    # Return the predicition as a probability array
    return (prediction, label_encoding[prediction], confidence)
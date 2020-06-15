#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
import sys
import json
from database_conn import *

# init the connection with the fetched environment variables
db_conn = init_connection(os.getenv('MYSQL_PASSWORD'), os.getenv('MYSQL_USER'))

# impose a limit on the results that can be returned by the database
MAX_RESULTS = 400

# create the flask application
app = Flask(__name__,
		template_folder = '/react_app/react_build/',
		static_folder = '/react_app/react_build/static/')

# allow cross origin requests to access the API
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# home page
@app.route('/')
@app.route('/home')
@app.route('/statistics')
@app.route('/endpoints')
def index():
	return render_template('index.html')

# API for querying threats
@app.route('/api/threats', methods=['GET'])
def get_threats():
	# impose a lower bound limit on the requests that can be fetched
	limit = min(request.args.get('limit', default = 30, type = int), MAX_RESULTS)

	# issue a prepared statement select to fetch the results
	results = execute_prepared_select(db_conn, '''SELECT DATE_FORMAT(date, \'%Y/%m/%d %H:%i:%S\'),
				prediction_type, src, dst, confidence FROM THREATS ORDER BY date DESC LIMIT ''' + str(limit) + ';', None)

	# instantiate a dictionary with the threats
	results_dict = {'threats': results}

	# return the jsonified dictionary
	return jsonify(results_dict)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=23231)

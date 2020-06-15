#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
import sys
import json
from database_conn import *

root_dir = os.path.dirname(os.path.abspath(__file__))
db_conn = init_connection(os.getenv('MYSQL_PASSWORD'), os.getenv('MYSQL_USER'))
MAX_RESULTS = 400

app = Flask(__name__,
		template_folder = '/react_app/react_build/',
		static_folder = '/react_app/react_build/static/')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
@app.route('/home')
@app.route('/statistics')
@app.route('/endpoints')
def index():
	return render_template('index.html')

@app.route('/api/threats', methods=['GET'])
def get_threats():
	limit = min(request.args.get('limit', default = 30, type = int), MAX_RESULTS)
	results = execute_prepared_select(db_conn, '''SELECT DATE_FORMAT(date, \'%Y/%m/%d %H:%i:%S\'),
				prediction_type, src, dst, confidence FROM THREATS ORDER BY date DESC LIMIT ''' + str(limit) + ';', None)
	results_dict = {'threats': results}
	return jsonify(results_dict)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=23231)

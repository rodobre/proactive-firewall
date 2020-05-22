#!/usr/bin/env python3
from flask import Flask, render_template
import os
import sys

root_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
		template_folder = root_dir + '/../react_build/',
		static_folder = root_dir + '/../react_build/')

@app.route('/')
@app.route('/home')
@app.route('/statistics')
@app.route('/endpoints')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')

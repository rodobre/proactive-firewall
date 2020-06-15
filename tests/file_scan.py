#!/usr/bin/python3
# All requests issued by this script should be labeled as File Scan / Crawling
import requests

url = 'http://icnc.go.ro:23231/'

if __name__ == '__main__':
	words = open('common.txt', 'r').readlines()
	for line in words:
		line = line.strip()
		r = requests.head(url + line, proxies={'http':'http://127.0.0.1:8080/'})
		print(r.text)

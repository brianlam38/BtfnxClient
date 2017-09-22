#!/usr/bin/python3

# Unofficial Bitfinex REST client
# 
# Author: Brian Lam
# Platforms: [ Bitfinex ]

import requests
import json
import sys
import hashlib
import hmac
import base64
import time

class BitfinexREST:

	def __init__ (self):
		self.key = None
		self.secret = None
		self.base = 'https://api.bitfinex.com'
		self.ver = '/v1/'
		self.auth_data = 0

	"""
	Grab keys from user provided filepath
	"""
	def add_keys(self, path):
		# open file
		f = open(path, 'r')
		keys = f.read()
		array = keys.split("\n")
		# store key + secret
		self.key = array[0]
		self.secret = array[1]

	"""
	Bitfinex authentication
	"""
	def auth(self, endpoint):
		# grab URL
		url = self.base + self.ver + endpoint
		# generate nonce
		nonce = str(int(time.time()) * 1000)
		# create param object
		param_obj = {
			'nonce': nonce,
			'url': url
		}
		# json encode param obj
		json_encoded = json.dumps(param_obj)
		print("json = {}".format(json_encoded))
		# base64 encode json obj
		payload = base64.b64encode(json_encoded.encode())
		print("payload = {}".format(payload))

		# create signature
		signature = None

		# create header data
		headers = {
			'X-BFX-APIKEY': self.key,			# API Public key
			'X-BFX-PAYLOAD': 'authentication',	# Payload = Params obj -> JSON encoded -> Base64 encoded
			'X-BFX-SIGNATURE': signature		# Signature = hex digest of HMAC-SHA384 hash(payload, api-secret)
		}

		return url, {'headers': headers}	# return full URL + HEADER obj

	"""
	POST method for auth calls
	"""
	def post(self, param):
		print("POST call")
		auth(param)
		return None

	"""
	GET method for public calls
	"""
	def get(self, param):
		print("GET call")
		return None


if __name__ == "__main__":

	# init Bitfinex restAPI
	b = BitfinexREST()

	# check program usage
	if len(sys.argv) < 2:
		print("Usage: Bitfinex.py key.txt")
		exit()

	# add keys to client object
	KEY_SECRET_PATH = sys.argv[1]
	b.add_keys(KEY_SECRET_PATH);
	b.auth('account_infos')

	####### test key + secret
	print(b.key)
	print(b.secret)
	#######



	# TICKER: get IOTA/USD pair state
	#response = requests.get('https://api.bitfinex.com/v1/pubticker/iotusd')
	#json_data = response.json()
	#print(json.dumps(json_data, indent=4))

	# REST AUTHENTICATED ENDPOINTS
	#headers = { "X-BFX-APIKEY": "../bitfinex.txt", "X-BFX-PAYLOAD": "../bitfinex.txt", "X-BFX-SIGNATURE": "../bitfinex.txt"}
	#response = requests.post('https://api.bitfinex.com/v1/account_infos', headers)
	#json_data = response.json()
	#print(json_data)
	#print(json.dumps(json_data, indent=4))


	# get and print Btfnx balance info
	#b = Bitfinex(key_file='../bitfinex.txt')	
	#response = b.balance()
	#json_data = response.json()
	#print(json_data[2]['amount'])

print("End of program")





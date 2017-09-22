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
#l
class BitfinexREST:

	def __init__ (self):
		self.public_key = None
		self.secret_key = None
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
		self.public_key = array[0]
		self.secret_key = array[1]

	"""
	Bitfinex authentication
	"""
	def auth(self, endpoint):
		# create param obj
		url = self.base + self.ver + endpoint
		nonce = str(int(time.time()) * 1000)
		param_obj = { 'nonce': nonce, 'url': url }

		# create payload: param obj -> json encode -> base64 encode
		json_encoded = json.dumps(param_obj)
		payload = base64.b64encode(json_encoded.encode())

		# initialise HMAC obj to verify integrity, 
		h = hmac.new(self.secret_key.encode(), payload, hashlib.sha384)
		signature = h.hexdigest()

		# create request header
		headers = {
			'X-BFX-APIKEY': self.public_key,	# Public key
			'X-BFX-PAYLOAD': payload,			# Payload = Params obj -> JSON encoded -> Base64 encoded
			'X-BFX-SIGNATURE': signature		# Signature = hex digest of HMAC-SHA384 hash(payload, api-secret)
		}

		return url, {'headers': headers}

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
	print(b.public_key)
	print(b.secret_key)
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






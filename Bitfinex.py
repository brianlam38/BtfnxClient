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

# test module
import Tests as T

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
	Generate nonce
	"""
	def nonce(self):
		nonce = str(int(time.time()) * 1000)
		return nonce

	"""
	Bitfinex authentication
	"""
	def auth(self, endpoint, nonce):
		# create param obj
		nonce = self.nonce()
		request = self.ver + endpoint
		param_obj = {
			'nonce': nonce,
			'request': request
		}

		# create payload: param obj -> json encode -> base64 encode
		json_encoded = json.dumps(param_obj)
		payload = base64.b64encode(json_encoded.encode())

		# initialise HMAC obj to verify integrity, set signature
		h = hmac.new(self.secret_key.encode(), payload, hashlib.sha384)
		signature = h.hexdigest()

		# create request header
		headers = {
			"X-BFX-APIKEY": self.public_key,	# Public key
			"X-BFX-PAYLOAD": payload,			# Payload = Params obj -> JSON encoded -> Base64 encoded
			"X-BFX-SIGNATURE": signature		# Signature = hex digest of HMAC-SHA384 hash(payload, api-secret)
		}

		return request, headers

	"""
	POST method for auth endpoints
	"""
	def post(self, req, headers):
		# parse response and ret json
		full_url = self.base + req
		response = requests.post(full_url, headers=headers)
		json = response.json()
		return json

	"""
	GET method for public endpoints
	"""
	def get(self, url):
		# parse response and ret json
		response = requests.get(url)
		json = response.json()
		return json



################
# Main Program
################

if __name__ == "__main__":

	# checking test module
	T.test()

	# init Bitfinex restAPI
	b = BitfinexREST()

	# check program usage
	if len(sys.argv) < 2:
		print("Usage: Bitfinex.py key.txt")
		exit()

	# TICKER: get IOTA/USD pair state
	#data = b.get(url)
	#print(json.dumps(data, indent=4))

	# add keys to instance
	KEY_SECRET_PATH = sys.argv[1]
	b.add_keys(KEY_SECRET_PATH)

	# generate url and request header
	request, headers = b.auth("account_infos", b.nonce)

	####### test nonce, public, secret
	print(b.nonce)
	print(b.public_key)
	print(b.secret_key)
	#######



	# REST AUTHENTICATED ENDPOINTS
	response = b.post(request, headers)
	print(response)







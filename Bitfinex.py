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
	def auth(self, endpoint):

		# generate nonce and request
		nonce = self.nonce()
		request = self.ver + endpoint

		# create param obj
		param_obj = {
			'nonce': nonce,
			'request': request,
			'currency': 'iot'
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

##################
# Public Endpoints
##################

# view current best bid-ask, last trade price, daily volume, price movement.
def get_ticker():
	return None

# view volume over a 1-7-30 day period.
def get_stats():
	return None

# view full margin funding book.
def get_funding_book():
	return None

# view full order book.
def get_order_book():
	return None

# view most recent trades.
# default: 50 items
def get_trades():
 	return None

# view list of most recent funding data.
# default: 50 items
def get_lends():
	return None

# view list of symbol names
def get_symbols():
	return None

# view list of symbol details
def get_symbol_details():
	return None

#########################
# Authenticated Endpoints
#########################

# Historical Data - Balance History
def balance_history(client):
	# generate url and request header
	request, headers = client.auth("hitory")

	# access endpoint
	data = client.post(request, headers)

	# print(json.dumps(data, indent=4))

	return data


################
# Main Program
################

if __name__ == "__main__":

	# check program usage
	if len(sys.argv) < 2:
		print("Usage: Bitfinex.py key.txt\n")
		print("key.txt format:")
		print("LINE 1: public key")
		print("LINE 2: private key")
		exit()

	# TICKER: get IOTA/USD pair state
	#data = b.get(url)
	#print(json.dumps(data, indent=4))

	# passing bitfinex obj to test module
	T.run_tests()




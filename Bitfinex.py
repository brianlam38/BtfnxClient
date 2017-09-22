#!/usr/bin/python3

# Unofficial Bitfinex REST client
# 
# Author: Brian Lam
# Platforms: [ Bitfinex ]

import requests
import json
import sys


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
	def addKeys(self, path):
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
	def auth(self, param):
		# grab URL
		url = self.base + self.ver + param
		###
		print(url)
		###
		# create signature
		signature = None
		# create header data
		headers = {
			'X-BFX-APIKEY': self.key,
			"X-BFX-SIGNATURE": signature,
			"X-BFX-PAYLOAD": 'authentication'

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

class userData:

	def __init__ (self):
		self.balance = 0
		self.profit = 0

	def initUserData(self):
		return None
		# update userData instance

	def setBalance(self):
		return None
		# set curr balance

	def setProfitN(self):
		return None
		# set profit Numeric

	def setProfitP(self):
		return None
		# set profit Percentage



if __name__ == "__main__":

	# init Bitfinex restAPI
	b = BitfinexREST()

	# check program usage
	if len(sys.argv) < 2:
		print("Usage: Bitfinex.py key.txt")
		exit()

	# add keys to client object
	KEY_SECRET_PATH = sys.argv[1]
	b.addKeys(KEY_SECRET_PATH);
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





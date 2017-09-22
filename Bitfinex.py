#!/usr/bin/python3

# Analysing Cryptocurrency Trade Performance
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
		self.url = 'https://api.bitfinex.com'
		self.ver = '/v1'
		self.auth_data = 0

	# Grab keys from filepath
	def addKeys(self, path):
		f = open(path, 'r')
		keys = f.read()
		array = keys.split("\n")
		# add to instance
		self.key = array[0]
		self.secret = array[1]

	# Bitfinex authentication
	def auth(self, key, secret, url, ver):

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

	# check correct usage
	if len(sys.argv) < 2:
		print("Usage: Bitfinex.py key.txt")
		exit()

	# grab filepath, keys and add to client object
	KEY_SECRET_PATH = sys.argv[1]
	b.addKeys(KEY_SECRET_PATH);

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





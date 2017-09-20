#!/usr/bin/python3

# Analysing Cryptocurrency Trade Performance
# 
# Author: Brian Lam
# Platforms: [ Bitfinex ]

import requests
import json
from bitex import Bitfinex

class userData:
	def __init__ (self):
		self.balance = 0
		self.profitN = 0	# numeric profit
		self.profitP = 0	# percentage profit

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

	# REST PUBLIC ENDPOINTS

	# TICKER: get IOTA/USD pair state
	response = requests.get('https://api.bitfinex.com/v1/pubticker/iotusd')
	json_data = response.json()
	#print(json.dumps(json_data, indent=4))



	# REST AUTHENTICATED ENDPOINTS
	headers = { "X-BFX-APIKEY": "../bitfinex.txt", "X-BFX-PAYLOAD": "../bitfinex.txt", "X-BFX-SIGNATURE": "../bitfinex.txt"}
	response = requests.post('https://api.bitfinex.com/v1/account_infos', headers)
	json_data = response.json()
	print(json_data)
	#print(json.dumps(json_data, indent=4))



	# get and print Btfnx balance info
	#b = Bitfinex(key_file='../bitfinex.txt')	
	#response = b.balance()
	#json_data = response.json()
	#print(json_data[2]['amount'])







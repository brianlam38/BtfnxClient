#!/usr/bin/python3

import json
from bitex import Bitfinex

import sys
sys.stdout = open('log.txt', 'w')

# Gather user data
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
	b = Bitfinex(key_file='../bitfinex.txt')

	# get and print ETH/USD pair info
	response = b.ticker('ethusd')
	json_data = response.json()
	#for item in json_data:
	#	print(item)

	#print(json_data)

	# get and print Btfnx balance info	
	#response = b.balance()
	#json_data = response.json()

	#print(json_data[0].currency)

	#for item in json_data:
	#	print(item.currency)




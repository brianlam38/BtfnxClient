#!/usr/bin/python3

# Analysing cryptocurrency trading performance
# 
# Author: Brian Lam
# Platforms: [ Bitfinex ]

import requests
import json
import sys

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

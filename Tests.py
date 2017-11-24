#!/usr/bin/python3

# Tests for Bitfinex REST client
# 
# Author: Brian Lam
# Platforms: [ Bitfinex ]

import Bitfinex as Bit
import traceback
import sys
import json

##################
# HELPER FUNCTIONS
##################


############
# MAIN TESTS
############
def run_tests():

	# overwrite old log
	f = open("stderr_log.txt", "w")
	f.close()

	# init Bitfinex object + add keys to instance
	b = Bit.BitfinexREST()
	KEY_SECRET_PATH = sys.argv[1]
	b.add_keys(KEY_SECRET_PATH)

	print("############# START OF TESTS #############\n")
	####### test public key
	print(b.public_key)
	#######

	print("--> Historical Data: Balance History")
	try:
		data = Bit.balance_history(b)
		print("Passed")
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		lines = traceback.format_exception(exc_type, exc_value, exc_traceback)

		f = open("stderr_log.txt", "+a")
		for line in lines:
			f.write(line)
		f.close()

		print("Failed")
		pass

	print("############# END OF TESTS #############")


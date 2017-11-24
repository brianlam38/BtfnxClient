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
def stderr_log():

	# grab exception/stack-trace as list of strings
	exc_type, exc_value, exc_traceback = sys.exc_info()
	lines = traceback.format_exception(exc_type, exc_value, exc_traceback)

	# write stack-trace to log
	f = open("stderr_log.txt", "+a")
	for line in lines:
		f.write(line)
	f.close()
	f.write("\n====================================================\n")

	print("Failed")

############
# MAIN TESTS
############
def run_tests():

	# overwrite old log content
	f = open("stderr_log.txt", "w")
	f.close()

	# init Bitfinex object + add keys to instance
	b = Bit.BitfinexREST()
	keys = sys.argv[1]
	b.add_keys(keys)

	print("############# START TESTS #############")

	try:
		print("--> Historical Data: Balance History")
		data = Bit.balance_history(b)
		print("Passed")
	except:
		stderr_log()
		pass

	try:
		print("--> Historical Data: Test 2")
		printf("lololol")
		print("Passed")
	except:
		stderr_log()
		pass

	try:
		print("stuff")
	except:
		pass

	try:
		print("stuff")
	except:
		pass

	print("############# END TESTS #############")


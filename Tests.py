#!/usr/bin/python3

# Tests for Bitfinex REST client
# 
# Author: Brian Lam
# Platforms: [ Bitfinex ]

def test(client):
	b = client
	print("testing module")
	####### test public key
	print(b.public_key)
	#######


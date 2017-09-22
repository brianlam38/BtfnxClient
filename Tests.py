#!/usr/bin/python3

# Tests for Bitfinex REST client
# 
# Author: Brian Lam
# Platforms: [ Bitfinex ]

def test(client):
	b = client
	print("testing module")
	####### test nonce, public, secret
	print(b.nonce)
	print(b.public_key)
	print(b.secret_key)
	#######


#!/usr/bin/python3

import requests
from bitex.api.REST.rest import BitfinexREST
from bitex.api.WSS.bitfinex import BitfinexWSS
from bitex.utils import return_api_response
from bitex.formatters.bitfinex import BtfxFormatter as fmt

b = BitfinexREST()
b.load_key('...')  # loads key and secret from given file;

# Query a public endpoint
response = b.query('GET','...', '...')
#print(response.json())

json_data = response.json()

print(json_data)

for item in json_data:
	print(item)

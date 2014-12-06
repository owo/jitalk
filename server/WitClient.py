#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wit 
import json

class WitClient(object):
	"""docstring for WitClient"""
	_access_token = 'NBPOVLY7T6W3KOUEML2GXOWODH3LPWPD'

	def __init__(self):
		wit.init()

	def text_query(self, text):
		res = json.loads(wit.text_query(text, WitClient._access_token))
		return res["outcomes"]
		
	def close_connection(self):
		wit.close()

if __name__ == "__main__":
	
	print "You ran the Wit client, nothing will happen. Exiting..."
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, get, request, Bottle
from FirebaseClient import *
from imojify import imojify_app

root = Bottle()
root.mount('imojify', imojify_app)

@root.get('/')
def server_root():
	return "WELCOME to jitalk"

@root.get('/firebase')
def firebase_client():
	# check the FirebaseClient class 

	firebaseInstance = FirebaseClient()
	
	# print firebaseInstance.postChat("-JcUVyYt9eBbWTWrw64V", "Mahmoud", "Order matters")
	# roomID = firebaseInstance.createRoom();

	return None

root.run(host='0.0.0.0', port=8080, debug=True)

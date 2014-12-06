#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, get, request
from FirebaseClient import *

@get('/imojify')
def api_imogify():
    sentence = request.query['sentence']
    src_lang = request.query['src_lang']

    return "Sentence: %s\n<br/>\nSource Language: %s" % (sentence, src_lang)

@get('/firebase')
def firebase_client():
	# check the FirebaseClient class 

	firebaseInstance = FirebaseClient()

	# print firebaseInstance.postChat("-JcUVyYt9eBbWTWrw64V", "Mahmoud", "Order matters")
	# roomID = firebaseInstance.createRoom();

	return None


run(host='0.0.0.0', port=8080, debug=True)

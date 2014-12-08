#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, get, request, Bottle, redirect, static_file, SimpleTemplate, TEMPLATE_PATH, template
from FirebaseClient import *
import json
import requests
import imojify
import translate
from random import randrange


TEMPLATE_PATH.insert(0, '../front-end/')

root = Bottle()


@root.get('/')
def server_root():

    return template('index')


@root.get('/favicon.ico')
def get_favicon():
    return server_static('favicon.ico')

# serve static files
@root.route('/static/<filename>')
def server_static(filename):
    root = "../front-end/"

    if filename.endswith(".css"):
        root = root + "css/"
    elif filename.endswith(".js"):
        root = root + "js/"
    elif filename.endswith(".jpg") or filename.endswith(".ico") or filename.endswith(".gif") or filename.endswith(".png") or filename.endswith(".svg"):
        root = root + "img/"
    else:
        root = root + "fonts/"

    return static_file(filename, root)


@root.get('/firebase')
def firebase_client():
    # check the FirebaseClient class 

    firebaseInstance = FirebaseClient()
    
    # firebaseInstance.postChat("-JcbLOjJBA29goO81X0T", "Mahmoud", "https://d30y9cdsu7xlg0.cloudfront.net/icon_uploads/f9de2428-8489-4e5e-b2c8-2c2bb3da667c.svg?Expires=1418004145&Signature=Er2laI8HftQwIgSYtvquXtT2Kh3AM6hf5T7adCsu4pLYAUFRuQWQYdrYA4N2XfuWQUhIEirUKNtONMyi2VvOXx4OvsLGjR6eZ-oD3NMJPJ4-esrgTsHtXb1MFP85WADw3-V7pMaSsgJYE383lHhRfcDBD~deEHTMLHdUeWV4UjY_&Key-Pair-Id=APKAI5ZVHAXN65CHVU2Q", "How are you?")
    # roomID = firebaseInstance.createRoom();

    return None


@root.get('/createRoom')
def create_room():

    firebaseInstance = FirebaseClient()
    roomID = firebaseInstance.createRoom()
    redirect('/room/'+roomID)


@root.get('/joinRandom')
def join_random_room():

    firebaseInstance = FirebaseClient()
    roomIDs = firebaseInstance.getRooms().keys()
    randMax = len(roomIDs)
    randomRoom = roomIDs[randrange(randMax)]
    redirect('/room/'+randomRoom)


@root.get('/room/<roomID>')
def chat_room(roomID):
    # you can share the room so others can join you
    # embed the roomID into the return page
    # return page
    
    return template('chatclient', roomID=roomID)


@root.get('/sendMessage')
def post_message():

    # this is not sending json for some reason
    # or this function can't parse
    username = request.query.username
    roomID = request.query.roomID
    text = request.query.text
    
    texts = []

    try:
        texts = imojify.imojify_input(translate.translate_to_english(text))
    except:
        pass  

    firebaseInstance = FirebaseClient()
    
    for sentence in texts:
        # roomID, username, decoded sentence, original text
        firebaseInstance.postChat(roomID, username, sentence, text)

    return "message has been sent!"


root.run(host='0.0.0.0', port=8080, debug=True)

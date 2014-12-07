#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, get, request, Bottle, redirect, static_file, SimpleTemplate, TEMPLATE_PATH, template
from FirebaseClient import *
import imojify


#TEMPLATE_PATH.insert(0, 'views/')

root = Bottle()


@root.get('/')
def server_root():
    return template('index', username="Mahmoud")


# serve static files
@root.route('/static/<filename>')
def server_static(filename):
    root = "../front-end/"

    if filename.endswith(".css"):
        root = root + "css/"
    elif filename.endswith(".js"):
        root = root + "js/"
    else:
        root = root + "fonts/"

    return static_file(filename, root)



@root.get('/firebase')
def firebase_client():
    # check the FirebaseClient class 

    firebaseInstance = FirebaseClient()
    
    # print firebaseInstance.postChat("-JcUVyYt9eBbWTWrw64V", "Mahmoud", "Order matters")
    # roomID = firebaseInstance.createRoom();

    return None


@root.get('/createRoom')
def create_room():
    firebaseInstance = FirebaseClient()
    roomID = firebaseInstance.createRoom()
    redirect('/room/'+roomID)


@root.get('/room/<roomID>')
def chat_room(roomID):
    # you can share the room so others can join you
    # embed the roomID into the return page
    # return page
    return roomID


@root.get('/sendMessage')
def post_message():
    #jsonData = json.load(request.json)
    #jsonData.data = {roomID: "", username: "", text: ""}
    firebaseInstance = FirebaseClient()
    texts = []

    try:
        texts = imojify.imojify_input(jsonData.data['text'])
    except:
        pass  
    
    return "message has been sent!"


root.run(host='0.0.0.0', port=8080, debug=True)

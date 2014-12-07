#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, get, request, Bottle, redirect, static_file, SimpleTemplate, TEMPLATE_PATH, template
from FirebaseClient import *
from imojify import imojify_app
from WitClient import *


# TEMPLATE_PATH.insert(0, './views')

root = Bottle()
root.mount('imojify', imojify_app)


@root.get('/')
def server_root():
    # return "WELCOME to jitalk"
    
    return template('index', None)


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


def handle_wit(objects):
    # object = {[{"_text":"How many hours left?","confidence":0.62,"entities":
    # {"object":[{"value":"many"},{"value":"hours lef"}],
    # "question":[{"value":"How"}]},"intent":"get_question"}]}

    is_question = False
    tokens = []

    if objects is not None and len(objects) > 0:
        for o in objects[0]:
            if 
    # object['entities'] = {"object":[{"value":"many"},{"value":"hours lef"}]
    
    return "HELLO"


@root.get('/sendMessage')
def post_message():
    #jsonData = json.load(request.json)
    #jsonData.data = {roomID: "", username: "", text: ""}
    wit = WitClient()
    firebaseInstance = FirebaseClient()
    
    response = wit.text_query("How many hours left?")
    
    
    wit.close_connection()
    return "message has been sent!"

root.run(host='0.0.0.0', port=8080, debug=True)

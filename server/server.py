#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, get, request, Bottle, redirect, static_file
from FirebaseClient import *
from imojify import imojify_app

root = Bottle()
root.mount('imojify', imojify_app)

@root.get('/')
def server_root():
    return "WELCOME to jitalk"

@root.get('/test/<file_name>')
def server_test(file_name):
    return static_file(file_name, root="/Users/mahmoudalismail/Hackathons/Koding/jitalk/server/front-end-files")
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
    jsonData = json.load(request.json)
    #jsonData.data = {roomID: "", username: "", text: ""}

root.run(host='0.0.0.0', port=8080, debug=True)

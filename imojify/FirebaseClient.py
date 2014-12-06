from firebase import firebase


class FirebaseClient(object):
	"""docstring for FirebaseClient"""
	
	_instance = None
	
	def __init__(self):
		if not FirebaseClient._instance:
			FirebaseClient._instance = firebase.FirebaseApplication('https://ji-talk.firebaseio.com', None)

	def getRooms(self):
		return FirebaseClient._instance.get('/', None)

	def getChat(self, roomID):
		return FirebaseClient._instance.get('/', roomID)

	def createRoom(self):
		# could be handled by the front-end
		# returns the room ID as a string in uni-8 unicoding
		roomID = FirebaseClient._instance.post('/', "chatRoom")
		return str(roomID['name'])

	def postChat(self, roomID, username, line):
		# roomID expected as a string
		data = {'username': username, 'line': line}
		return FirebaseClient._instance.post('/'+roomID, data)


if __name__ == "__main__":
	
	print "You ran the client, nothing will happen. Exiting..."

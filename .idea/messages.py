import socket
import globals

class Message:
    def __init__(self, username, function, body=""):
        self.username = username
        self.function = function
        self.body = body
    def __str__(self):
        return string_from_message(self)

def message_from_string(message):
	lines = message.splitlines()
	if len(lines) == 0:
		return 0
	user = lines[0].split(' ')[1]
	func = lines[1].split(' ')[1]
	body = '\n'.join(lines[3:])
	return Message(user, func, body)

def string_from_message(message):
	out = str()
	out += "USER: " + message.user + "\r\n"
	out += "FUNC: " + message.func + "\r\n"
	out += "\r\n"
	out += message.body
	return out

def send_message(to_sock, msg_obj):
	# Takes a message object, returns bytes sent
	msg_str = string_from_message(msg_obj)
	sentBytes = network_send_message(to_sock, msg_str)
	return sentBytes != 0

def recv_message(from_sock):
	# Returns a Message object
	recv_str = network_recv_message(from_sock, MAX_MSG_LEN)
	msg_obj = message_from_string(recv_str)
	return msg_obj

def network_send_message(to_sock, message):
	'''
	Wrapper for socket sending, encodes for you
	'''
	sentBytes = to_sock.send(message.encode())
	return sentBytes

def network_recv_message(from_sock, buf_len):
	'''
	Wrapper for socet receiving, decodes for you
	'''
	recv = from_sock.recv(buf_len)
	return recv.decode()
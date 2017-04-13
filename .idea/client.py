import sys, threading, socket
import leaderboard, util, globals
from messages import *

class Client:
    def __init__(self, serverInfo, username):
        self._username = username
        self._serverInfo = serverInfo

    # Public
    def add_entry(self, entry):
        entry_string = entry_to_string(entry)
        entry_message = Message(self._username, globals.FUNC_ADD_ENTRY, entry_string)
        return self._send_msg_and_process_response(entry_message)

    def request_leaderboard(self):
        request = Message(self._username, globals.FUNC_REQUEST_LEADERBOARD)
        return self._send_msg_and_process_response(request)

    #Private
    def _connect(self, serverInfo):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect( (serverInfo["serverName"], int(serverInfo["portNumber"])) )
        return sock

    def _handle_message(self, message):
        if message.func == globals.FUNC_SEND_LEADERBOARD:
            return message.body

    def _send_msg_and_process_response(self, message):
        serv_sock = self._connect(self._serverInfo)
        send_message(self._socket, message)
        serv_response = recv_message(self.sock)
        retval = self._handle_message(serv_response)
        serv_sock.close()
        return retval

if __name__=="__main__":
    util.clear_screen()

    if len(sys.argv) < 3:
        print("Error: Correct format 'client.py server portno'")
        exit()
    serverInfo = {}
    serverInfo["serverName"] = sys.argv[1]
    serverInfo["portNumber"] = sys.argv[2]

    user = input("Username: ")
    client = Client(serverInfo, user)
    print(client.request_leaderboard())
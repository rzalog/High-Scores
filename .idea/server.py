import sys, threading, socket, select
import globals
from messages import *
from leaderboard import *

class Server:
    def __init__(self, portno):
        self._socket = self._init_socket(portno)
        self._leaderboard = self._init_default_leaderboard()

    # Public
    def start(self):
        print("Server initialized, waiting for connections")
        while True:
            client_sock, addr = self._socket.accept()
            client_msg = recv_message(client_sock)
            print("Connected to client, username {}".format(client_msg.username))
            response = self._handle_message(client_msg)
            send_message(client_sock, response)
            print("Connection to client '{}' closed.".format(client_msg.username))
            client_sock.close()

    # Private
    def _init_socket(self, portno):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind( ('', portno) )
        sock.listen(10)
        return sock

    def _handle_message(self, message):
        if message.func == globals.FUNC_REQUEST_LEADERBOARD:
            print("Request for leaderboard from user {}".format(message.username))
            response = Message(globals.USER_SERVER, globals.FUNC_SEND_LEADERBOARD, str(self._leaderboard))
        if message.func == globals.FUNC_ADD_ENTRY:
            print("Add entry from user {}".format(message.username))
            entry = entry_from_string(message.body)
            self._leaderboard.add_entry(entry)
            response = Message(globals.USER_SERVER, globals.FUNC_ACK)
        return response

    def _init_default_leaderboard(self):
        title = "Pacman high scores"
        keys = ["Name", "Version"]
        options = {"valueLabel": "Score"}
        key = lambda a: a.value
        leaderboard = Leaderboard(title, options, keys, key)

        entries = []
        entries.append(LeaderboardEntry(["Robert", "Pacman"], 150))
        entries.append(LeaderboardEntry(["Max", "Ms. Pacman"], 180))
        entries.append(LeaderboardEntry(["Jiwan", "Pacman and Friends"], 120))

        for entry in entries:
            leaderboard.add_entry(entry)

        return leaderboard

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Error: Format should be 'server.py portno'.")
        exit()
    server = Server(int(sys.argv[1]))
    server.start()
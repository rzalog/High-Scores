#!/usr/local/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
	# GET
	def do_GET(self):

		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

		message = "Hello, world!"
		self.wfile.write(bytes(message, 'utf8'))

		if self.rfile.readable():
			print(self.rfile.readline())
		else:
			print("rfile is not readable")

		return

	# POST
	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		# contentLength = int(self.headers.getheader('Content-Length'))
		self.rfile.read(100)

def run():
	print('Starting server...')

	server_addr = ('localhost', 8080)
	httpd = HTTPServer(server_addr, MyHTTPRequestHandler)
	print('Running server (forever)...')
	httpd.serve_forever()

run()
# * [X] numbers
# * [X] strings
# * [X] arrays,lists,sets
# abstract types

# from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from http.server import BaseHTTPRequestHandler

class Plant:
    def __init__(self):
        self.height = 0

    def grow(self):
        old_height = self.height
        self.height = old_height + 1

plant = Plant()
other_plant = Plant()

print(plant.height)
print(other_plant.height)

plant.grow()

print(plant.height)
print(other_plant.height)

for item in range(1,10):
    plant.grow()

print(plant.height)

import http.server
import socketserver

PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def __init__(self, *args):
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('X-Custom-Thing', 'kelly')
        self.end_headers()
        with open('index.html', 'rb') as file:
            self.wfile.write(file.read())
        return

    def do_POST(self):
        self.send_response(301)
        self.send_header('Location', '/')
        self.end_headers()
        self.send_response(301)
        return

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

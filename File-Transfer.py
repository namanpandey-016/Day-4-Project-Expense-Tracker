#A simple program to transfer file between two devices connected with same internet
import http.server
import socketserver
PORT = 8000
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as http:
    print("server running on port", PORT)
    http.serve_forever()

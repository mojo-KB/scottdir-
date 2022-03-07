from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

port = 8080
host = '127.0.0.1'
server_address = (host,port) 
httpd = HTTPServer(server_address,CGIHTTPRequestHandler)
print("Starting my web server on port "+str(port))
httpd.serve_forever()


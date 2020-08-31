import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

    #Use this file to start the server, command: python -m SimpleHTTPServer 8080

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8080
#use local IP
#server_address = ('14.129.94.28', port)
server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()

#!/usr/bin/python3.7

import http.server
import socketserver
import re

PORT=8001

class Myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if re.match("/\?foo/\d+", self.path):
            number = str_fac(self.path)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(str(number), "utf-8"))
            return
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes("hell-o", "utf-8"))
            return

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def str_fac(string):
    num = int(string.split("/")[-1])
    return fac(num)

with socketserver.TCPServer(("", PORT), Myhandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()

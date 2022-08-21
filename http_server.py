#!/bin/env python3
import json
from http.server import BaseHTTPRequestHandler,HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()

        message = {'a':'1'}
        self.wfile.write(bytes(json.dumps(message),"utf-8"))

with HTTPServer(("127.0.0.1",8000),Handler) as server:
    server.serve_forever()


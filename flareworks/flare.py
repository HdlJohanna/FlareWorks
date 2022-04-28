from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer as HTTPServer
from typing import SupportsIndex

from .response import Response
from .routing import HTTPMap, Rule
from .globals import Request

class RequestCtxManager(BaseHTTPRequestHandler):
    
    def do_GET(self):
        route:HTTPMap = self.flare.map
        r = route.get_rule(self.path)
        request = Request(self)
        if not r:
            self.send_response(404)
            self.wfile.write("<h1>404 Not found</h1>. If you entered the URL manually please check your spelling and try again".encode())
            return

        if "GET" in r.methods:
            result = r.function(request)
            if isinstance(result,tuple):
                self.send_response(result[1])
                self.wfile.write(result[0].encode())
            else:
                if hasattr(result,"__mimetype__"): # The Object *is* a Response-Object
                    self.send_response(result.__status__)
                    self.send_header("content-type",result.__mimetype__)
                    for key, val in result.__headers__.contents:
                        self.send_header(key, val)
                else:
                    self.send_response(200)
                    self.wfile.write(result.encode())

    def do_POST(self):
        route:HTTPMap = self.flare.map
        r = route.get_rule(self.path)
        request = Request(self)
        request.body = self.rfile
       
        if not r:
            self.wfile.write("<h1>404 Not found</h1>. If you entered the URL manually please check your spelling and try again".encode())
        if "POST" in r.methods:
            result = r.function(request)
            if isinstance(result,tuple):
                self.send_response(result[1])
                self.wfile.write(result[0].encode())
            else:
                self.send_response(200)
                self.wfile.write(result.encode())
        


class FlareWork:
    def __init__(self,import_name):
        self.__name__ = import_name
        self.map = HTTPMap([])
        self.ctx_man = RequestCtxManager
        self.ctx_man.flare = self

    def path(self,endpoint,**kwds):
        
        def predicate(f):
            self.map.add_rule(Rule(endpoint,self,f,kwds.get("methods",["GET"])))

        return predicate

    def run(self,host="localhost",port=8000):
        server = HTTPServer((host,port),self.ctx_man)
        print(f" * Running as {self.__name__} on http://{host}:{port}")
        while True:
            server.handle_request()
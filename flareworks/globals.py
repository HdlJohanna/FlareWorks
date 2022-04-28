from http.server import BaseHTTPRequestHandler
from collections import namedtuple
from typing import List, Union
import typing

class Request:
    def __init__(self,incoming:BaseHTTPRequestHandler):
        self.method = incoming.command
        self._sock = incoming.connection
        _remote = namedtuple("remote", 'addr port')
        self.remote = _remote(*incoming.client_address)
        self.headers = Headers([])
        for k in incoming.headers.keys():
            self.headers.add([k,incoming.headers.get(k)])



class Headers:
    def __init__(self,contents:Union[List[tuple], None]):
        self.contents = contents or []

    def __getitem__(self,value):
        for key,val in self.contents:
            if key == value:
                return val
        
        return None

    def add(self,__seq:tuple):
        self.contents.append(__seq)
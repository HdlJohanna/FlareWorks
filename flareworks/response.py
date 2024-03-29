import json
from .globals import Headers
from .routing import Rule
import typing

class Redirect:
    """
    Implements Redirects using the REFRESH Http Header. Since flare.RequestCtxManager doesn't do Class Checks
    but instead checks for Attributes, all we have to do is set the __redirect__ property.

    This class also has a `.__mimetype__` but you don't have to care about that
    
    >>> @app.path("/redirect")
    >>> def rdr_to(request):
    >>>     return Redirect("/")

    >>> redirect = rdr_to(None)
    >>> redirect.__status__
    308
    >>> redirect.__mimetype__
    'text/plain'
    
    """
    def __init__(self, endpoint, status=308,redirect_after=0):
        self.__headers__ = Headers([("refresh",f"{redirect_after};url={endpoint}")])
        self.__status__ = status
        self.__mimetype__ = "text/plain"
        self.__redirect__ = True

class Response(str):
    """
    Base class to return different MIMETypes and Headers, as returning a String will set the Content-Type to text/plain, with no Headers, 
    whereas a `Response` Object can return different MIMETypes, defaulting to text/html

    >>> @app.path("/")
    >>> def root(request):
    >>>     return "This is plain Text, <h1>No matter the Formatting</h1>"

    >>> @app.path("/2")
    >>> def with_response(request):
    >>>     return Response("<h1>Hello world!</h1>")

    >>> response = with_response(None)
    >>> response.__mimetype__
    'text/html'
    """

    def __init__(self, *args, mimetype="text/html", status=200, headers:Headers = Headers([()])) -> None:
        super().__init__()
        self.body = " ".join(args)
        self.__status__ = status
        self.__mimetype__ = mimetype
        self.__headers__ = headers
        self.__headers__.add(("server","0.0.0.0"))

class JSON(Response):
    def __init__(self,*args):
        """
        A Response-Like Object with a jsonfied body.
        Do not invoke this Function directly! Use `.jsonify` instead

        >>> @app.path("/")
        >>> def json_method(request):
        >>>     return jsonify({"ResponseCode":200})

        >>> response = json_method(None)
        >>> response.__mimetype__
        'application/json'
        """

        super().__init__(json.dumps(args[0]),mimetype="application/json",status=200)

def jsonify(obj,**kwargs):
    resulting = {}
    for k in obj.keys():
        resulting[k] = obj.get(k)
    for k in kwargs.keys():
        resulting[k] = kwargs.get(k)
    print(resulting)
    return JSON(json.dumps(resulting))

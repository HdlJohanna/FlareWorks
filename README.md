# FlareWorks - Simple, Lightweight Python 3 Webserver
FlareWorks is a Microframework to create Websites within Minutes.  

```py
from flareworks import FlareWork
from flareworks.response import Response

app = FlareWork(__name__)

@app.path("/")
def slash(request):
    return Response("Hello World!")

app.run()
```

And if you understand this code, you understood the entire Framework

# Flask

## Installation
Install memakai __pip__
```
$ pip install flask
$ pip install flask_restful
$ pip install flask_cors
```
## Return Text

```python
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

application = app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Hello World"

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

## Return Text with Argument

```python
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

application = app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Hello World"

api.add_resource(HelloWorld, '/')

class Name(Resource):
    def get(self, nama, umur):
        return "Hello " + nama+umur

api.add_resource(Name, '/nama/<nama>/<umur>')

if __name__ == '__main__':
    app.run(debug=True)
```

## Return Image

```python
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import 

application = app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Hello World"

api.add_resource(HelloWorld, '/')

class Name(Resource):
    def get(self, nama, umur):
        return "Hello " + nama+umur

api.add_resource(Name, '/nama/<nama>/<umur>')

class getImage(Resource):
    def get(self, skor):
        filename = drawing.Draw(skor)
        return send_file(filename, mimetype='image/png')

api.add_resource(getImage, '/getlogo')


if __name__ == '__main__':
    app.run(debug=True)
```
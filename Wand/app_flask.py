import sys
import os

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import send_file

import app_wand as drawing

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

class getLogoChelsea(Resource):
    def get(self, skor):
        filename = drawing.Draw(skor)
        return send_file(filename, mimetype='image/png')

api.add_resource(getLogoChelsea, '/getlogo/<skor>')


if __name__ == '__main__':
    app.run(debug=True)

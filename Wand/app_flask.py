import sys
import os

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import send_file

import app_wand as wa

application = app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World!'}

api.add_resource(HelloWorld, '/')

class GetVoucher(Resource):
    def get(self, body):
        filename = './score-output.png'
        return send_file(filename, mimetype='image/png')

api.add_resource(GetVoucher, '/draw/score/<body>')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_restful import Resource, Api
from app.resources.message import Message

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Message, '/message', methods=['POST'])

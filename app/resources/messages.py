from flask_restful import Resource
from flask import request
from flask import jsonify
from app.domain_model.domain import Message
from app.services.saver import Saver


class Messages(Resource):

    """Messages are immutable, they can only be created and archived."""

    def get(self, id):
        resp = jsonify({'status': "ok"})
        resp.status_code = 200
        return resp

    def post(self):
        message_json = request.get_json()
        message = Message(message_json['to'], message_json['from'], message_json['body'])
        message_service = Saver()
        message_service.saveMessage(message)
        resp = jsonify({'status': "ok"})
        resp.status_code = 200
        return resp


from flask_restful import Resource
from flask import request
from flask import jsonify
from app.domain_model.domain import Message
from app.services.saver import Saver
# use constructor to create dependencies, loose coupling

class Send(Resource):

    def get(self):
        pass

    def post(self):
        message_json = request.get_json()
        message = Message(message_json['to'], message_json['from'], message_json['body'])
        messageService = Saver()
        messageService.saveMessage(message)
        content = {'status': "ok"}
        resp = jsonify(content)
        resp.status_code = 200
        return resp


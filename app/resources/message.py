from flask_restful import Resource
from flask import request
from flask import jsonify
from app.data_model.model import SecureMessage
from app.data_model.model import db

class Message(Resource):

    def get(self):
        pass

    def post(self):
        message = request.get_json()
        secure_message = SecureMessage(message['to'], message['from'], message['body'])
        db.session.add(secure_message)
        db.session.commit()
        content = {'status': "ok"}
        resp = jsonify(content)
        resp.status_code = 200
        return resp


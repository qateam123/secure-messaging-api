from flask_restful import Resource, reqparse
from flask import request
from flask import jsonify
from app.data_model.model import SecureMessage
from app.data_model.model import db
from marshmallow import Schema, fields, post_load

class Message(Resource):

    def __init__(self, msg_to, msg_from, body):
        self.msg_to = msg_to
        self.msg_from = msg_from
        self.body = body

    def __repr__(self):
        return '<Message(msg_to={self.msg_to} msg_from={self.msg_from} body={self.body})>'.format(self=self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

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

class MessageSchema(Schema):
    msg_to = fields.Str()
    msg_from = fields.Str()
    body = fields.Str()

    @post_load
    def make_message(self, data):
        return Message(**data)


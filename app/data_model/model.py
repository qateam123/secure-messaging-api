from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, post_load

db = SQLAlchemy()

class SecureMessage(db.Model):

    __tablename__ = "secure_message"
    id = Column(Integer, primary_key=True)
    msg_to = Column("msg_to", String)
    msg_from = Column("msg_from", String)
    body = Column("body", String)
    # submitted_at = Column("submitted_at", DateTime)

    def __init__(self, msg_to, msg_from, body):
        self.msg_to = msg_to
        self.msg_from = msg_from
        self.body = body
        # self.submitted_at = datetime.now()

class Message():

    def __init__(self, msg_to, msg_from, body):
        self.msg_to = msg_to
        self.msg_from = msg_from
        self.body = body
        # self.submitted_at = datetime.now()

    def __repr__(self):
        return '<Message(msg_to={self.msg_to} msg_from={self.msg_from} body={self.body})>'.format(self=self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class MessageSchema(Schema):
    msg_to = fields.Str()
    msg_from = fields.Str()
    body = fields.Str()

    @post_load
    def make_message(self, data):
        return Message(**data)
from marshmallow import Schema, fields, post_load


class Message:

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

    """ Class to marshal JSON to Message"""

    msg_to = fields.Str()
    msg_from = fields.Str()
    body = fields.Str()

    @post_load
    def make_message(self, data):
        return Message(**data)

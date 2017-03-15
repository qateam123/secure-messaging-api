import unittest
import json
from app.domain_model.domain import Message, MessageSchema
import sys

class MessageTestCase(unittest.TestCase):

    def testMarshalJson(self):
        message = Message('richard', 'torrance', 'hello')
        schema = MessageSchema()
        json_result = schema.dumps(message)
        message_load = schema.load(json.loads(json_result.data))
        self.assertTrue(message_load.data == message)

    def test_msg_to_validation_true(self):
        message = {'msg_to':'richard', 'msg_from':'torrance', 'body':'hello'}
        schema = MessageSchema()
        data, errors = schema.load(message)
        self.assertTrue(errors == {})

    def test_msg_to_max_length_validation_false(self):
        msg_to = "x" * 101
        message = {'msg_to': msg_to, 'msg_from':'torrance', 'body':'hello'}
        schema = MessageSchema()
        data, errors = schema.load(message)
        self.assertTrue(errors == {'msg_to': ['Quantity must not be greater than 100.']})

    def test_msg_to_min_length_validation_false(self):
        message = {'msg_to': '', 'msg_from':'torrance', 'body':'hello'}
        schema = MessageSchema()
        data, errors = schema.load(message)
        self.assertTrue(errors == {'msg_to': ['Quantity must be greater than 0.']})

    def test_msg_to_required_validation_false(self):
        message = {'msg_from':'torrance', 'body':'hello'}
        schema = MessageSchema()
        data, errors = schema.load(message)
        print(errors, file=sys.stderr)
        self.assertTrue(errors == {'msg_to': ['Missing data for required field.']})

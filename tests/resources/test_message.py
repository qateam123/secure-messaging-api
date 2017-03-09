import unittest
import json
from app.resources.message import Message, MessageSchema

class MessageTestCase(unittest.TestCase):

    def testMarshalJson(self):
        message = Message('richard', 'torrance', 'hello')
        schema = MessageSchema()
        json_result = schema.dumps(message)
        message_load = schema.load(json.loads(json_result.data))
        self.assertTrue(message_load.data == message)
import unittest
from flask import json
import sys
sys.path.append('../secure-messaging-api')
from app import application
from app import settings
from sqlalchemy import create_engine

class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = application.app.test_client()
        # propagate the exceptions to the test client
        #self.app.testing = True

    def test_home_status_code(self):
        '''sends HTTP GET request to the application
        on the specified path'''
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_post_request_message_goes_to_database(self):
        # post json message written up in the ui
        url = "http://localhost:5050/message"
        data = {'to': "Emilio", 'from': "Tej", 'body': "Hello World"}
        headers = {'Content-Type': 'application/json'}
        response = self.app.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(json.loads(response.get_data()), {'status': "ok"})


    def test_that_checks_post_request_is_within_database(self):
        #check if json message is inside the database
        engine = create_engine(settings.SECURE_MESSAGING_DATABASE_URL, echo=True)
        data={}
        with engine.connect() as con:
            request = con.execute('SELECT * FROM secure_message WHERE id = (SELECT MAX(id) FROM secure_message)')
            for row in request:
                data={"to": row['msg_to'], "from": row['msg_from'], "body": row['body']}
                # print("to:", row['msg_to'], "from:", row['msg_from'], "body:", row['body'])
                self.assertEqual({'to': 'Emilio', 'from': 'Tej', 'body': 'Hello World'},data)
                #con.close()

    # def tearDown(self):
    #     # Closing down the database
    #     self.db.session.remove()
    #     self.db.drop_all()

if __name__ == '__main__':
    unittest.main()

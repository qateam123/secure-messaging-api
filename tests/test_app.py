import sys
import unittest
sys.path.append('../secure-messaging-api')
from app import api


class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = api.app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()

from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from app.database import db_session
from app.resources.message import Message

'''
Root level endpoint for secure messaging api
'''

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

api.add_resource(HelloWorld, '/')
api.add_resource(Message, '/message/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)

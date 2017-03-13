from flask import Flask
from flask_restful import Resource, Api
from app.resources.send import Send
from structlog import get_logger
from app.data_model import database
from app import settings

logger = get_logger()

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SECURE_MESSAGING_DATABASE_URL
database.db.init_app(app)

with app.app_context():
     database.db.create_all()
     database.db.session.commit()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Send, '/send', methods=['POST'])

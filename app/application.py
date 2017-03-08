from flask import Flask
from flask_restful import Resource, Api
from app.resources.message import Message
from structlog import get_logger
from app.data_model import model
from app import settings

logger = get_logger()

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SECURE_MESSAGING_DATABASE_URL
model.db.init_app(app)

with app.app_context():
     model.db.create_all()
     model.db.session.commit()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Message, '/message', methods=['POST'])

from flask import Flask
from flask_restful import Resource, Api
from app.resources.messages import Messages, MessagesById
from app.resources.health import Health
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

api.add_resource(Health, '/health')
api.add_resource(Messages, '/messages/send', '/messages', methods=['POST', 'GET'])
api.add_resource(MessagesById, '/messages/<int:id>', methods=['GET', 'PUT'])

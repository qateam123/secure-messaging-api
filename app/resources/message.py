from flask_restful import Resource
from flask import request
from flask import jsonify
from app.model import SecureMessage
from app.database import db_session, commit_or_rollback

class Message(Resource):

    def get(self):
        pass

    def post(self):
        message = request.get_json()

        secure_message = SecureMessage(message['to'], message['from'], message['body'])

        try:
            with commit_or_rollback(db_session):
                db_session.add(secure_message)
        except BaseException as error:
            return jsonify(result="false")

        content = {'status': "ok"}
        resp = jsonify(content)
        resp.status_code = 200

        return resp

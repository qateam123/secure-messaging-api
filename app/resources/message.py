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
        #message = {'to': "toPerson", 'from': "fromPerson", 'body': "body stuff"}

        try:
            secure_message = SecureMessage(message['to'], message['from'], message['body'])
        except BaseException as error:
            return jsonify(result="could not make message", error=str(error))
            #logger.info("DID NOT CREATE FEEDBACK RESPONSE: " + str(error))

        try:
            #logger.info("using commit_or_rollback")
            with commit_or_rollback(db_session):
                #logger.info("ADDING ON TO SESSION")
                db_session.add(secure_message)
        except BaseException as error:
            #logger.info("Database commit failed: " + str(error))
            return jsonify(result="false")

        content = {'status': "ok"}
        resp = jsonify(content)
        resp.status_code = 200

        return resp

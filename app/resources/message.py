from flask_restful import Resource

class Message(Resource):

    def get(self, id):
        return "This is message {}".format(id)

    def post(self):
        pass
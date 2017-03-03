from sqlalchemy import Column, String, DateTime, Integer
from app.database import base
from datetime import datetime


class SecureMessage(base):
    __tablename__ = "secure_message"
    id = Column(Integer, primary_key=True)
    msg_to = Column("msg_to", String)
    msg_from = Column("msg_from", String)
    body = Column("body", String)
    #secure__id = Column("eq_session_id", String, primary_key=True)
    #user_id = Column("user_id", String, primary_key=True)
    submitted_at = Column("submitted_at", DateTime)

    def __init__(self, msg_to, msg_from, body):
        self.msg_to = msg_to
        self.msg_from = msg_from
        self.body = body
        self.submitted_at = datetime.now()

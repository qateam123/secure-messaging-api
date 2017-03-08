from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SecureMessage(db.Model):
    __tablename__ = "secure_message"
    id = Column(Integer, primary_key=True)
    msg_to = Column("msg_to", String)
    msg_from = Column("msg_from", String)
    body = Column("body", String)
    submitted_at = Column("submitted_at", DateTime)

    def __init__(self, msg_to, msg_from, body):
        self.msg_to = msg_to
        self.msg_from = msg_from
        self.body = body
        self.submitted_at = datetime.now()
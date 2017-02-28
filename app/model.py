from sqlalchemy import Column, String, DateTime
from app.database import base


class SecureMessage(base):
    __tablename__ = "secure_message"
    secure__id = Column("eq_session_id", String, primary_key=True)
    user_id = Column("user_id", String, primary_key=True)
    timestamp = Column("timestamp", DateTime)
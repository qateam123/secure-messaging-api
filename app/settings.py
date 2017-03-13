import os

SECURE_MESSAGING_DATABASE_URL = os.getenv('SECURE_MESSAGING_DATABASE_URL', 'sqlite:////tmp/messages.db')
# postgres://rasmessage:rasmessage@localhost:5432/messages

import os

SECURE_MESSAGING_DATABASE_URL = os.getenv('SECURE_MESSAGING_DATABASE_URL', 'postgres://rasmessage:rasmessage@localhost:6500/messages')
#postgres://rasmessage:rasmessage@172.28.93.106:6500/messages
#postgres://rasmessage:rasmessage@db:5432/messages

from structlog import get_logger
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from app import settings

logger = get_logger()
logger.debug("creating db engine")
engine = create_engine(settings.SECURE_MESSAGING_DATABASE_URL, convert_unicode=True)

logger.debug("creating database session")
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
base = declarative_base()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import app.model
    base.metadata.create_all(bind=engine)
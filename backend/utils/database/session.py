from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common.config import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()
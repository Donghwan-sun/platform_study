from sqlalchemy import Column, String, Integer, Date, Boolean, DateTime
from utils.database.base_class import Base
from utils.times import now_time

class Users(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    at_created = Column(Date, default=now_time())
    at_modify = Column(DateTime, default=now_time())
    is_superuser = Column(Boolean, default=False)
    
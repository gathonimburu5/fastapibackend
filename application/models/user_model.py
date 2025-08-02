from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timedelta
from application.config import Base

class Signup(Base):
    __tablename__ = 'signups'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email_address = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    status = Column(String, default="active", nullable=False)
    profile_picture = Column(String, nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow)

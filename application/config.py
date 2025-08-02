from urllib.parse import quote
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

# getting sensitive data from environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Database configuration
DB_USERNAME = "postgres"
DB_PASSWORD = quote(os.getenv("DATABASE_PASSWORD"))
POSTGRES_URL = "127.0.0.1"
POSTGRES_DB = os.getenv("DATABASE_NAME")
POSTGRES_PORT = 5432
DB_URL = 'postgresql://{user}:{pswd}@{url}:{port}/{db}?application_name=skoteApp'.format(user=DB_USERNAME, pswd=DB_PASSWORD, url=POSTGRES_URL, port=POSTGRES_PORT, db=POSTGRES_DB)

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
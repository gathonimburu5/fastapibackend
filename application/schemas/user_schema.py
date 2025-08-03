from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    id: int
    full_name: str
    email_address: EmailStr
    phone_number: str
    username: str
    password: str
    date_of_birth: date
    profile_picture: str | None = None
    status: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserToken(BaseModel):
    access_token: str
    token_type: str
    id: int
    full_name: str
    email_address: EmailStr
    phone_number: str
    username: str



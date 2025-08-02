from pydantic import BaseModel, EmailStr
from datetime import date

class UserBase(BaseModel):
    id: int
    full_name: str
    email_address: EmailStr
    phone_number: str
    username: str
    password: str
    date_of_birth: date
    profile_picture: str | None = None
    status: str = "active"

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    full_name: str
    email_address: EmailStr

    class Config:
        orm_mode = True


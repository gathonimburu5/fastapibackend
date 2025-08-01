from pydantic import BaseModel
from datetime import date

class EmployeeBase(BaseModel):
    id: int
    employee_name: str
    email_address: str
    id_number: str
    phone_number: str
    department: str
    postal_address: str
    date_of_birth: date
    date_of_joining: date
    physical_address: str
    designation: str
    salary: float

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int
    class Config:
        orm_mode = True


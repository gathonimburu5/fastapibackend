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

class CustomerBase(BaseModel):
    id: int
    customer_name: str
    email_address: str
    phone_number: str
    postal_address: str
    physical_address: str
    date_of_birth: date
    date_of_registration: date
    vat_pin: str
    credit_limit: float
    sales_rep_id: int
    status: str
    opening_balance: float
    opening_balance_date: date
    opening_balance_rate: float
    currency_id: int

class CustomerCreate(CustomerBase):
    pass
class CustomerOut(CustomerBase):
    id: int
    class Config:
        orm_mode = True
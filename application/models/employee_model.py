from sqlalchemy import Column, Integer, String, Float, DateTime
from application.config import Base
from datetime import datetime

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String, index=True, nullable=False)
    email_address = Column(String, unique=True, index=True, nullable=False)
    id_number = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    department = Column(String, nullable=False)
    postal_address = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    date_of_joining = Column(DateTime, nullable=False)
    physical_address = Column(String, nullable=False)
    designation = Column(String, nullable=False)
    salary = Column(Float, nullable=False, default=0.0)
    status = Column(String, default="active", nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String, nullable=False)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True, nullable=False)
    email_address = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    postal_address = Column(String, nullable=False)
    physical_address = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    date_of_registration = Column(DateTime, nullable=False)
    vat_pin = Column(String, unique=True, index=True, nullable=False)
    credit_limit = Column(Float, nullable=False, default=0.0)
    sales_rep_id = Column(Integer, nullable=False)
    status = Column(String, default="active", nullable=False)
    opening_balance = Column(Float, default=0.0, nullable=False)
    opening_balance_date = Column(DateTime, nullable=True)
    opening_balance_rate = Column(Float, default=0.0, nullable=False)
    currency_id = Column(Integer, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String, nullable=False)
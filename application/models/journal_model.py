from sqlalchemy import Column, String, Integer, Float, Date
from application.config import Base
from datetime import datetime

class JournalHeader(Base):
    __tablename__ = 'journal_header'

    id = Column(Integer, primary_key=True, index=True)
    journal_description = Column(String, nullable=False)
    journal_date = Column(Date, nullable=False)
    transaction_period = Column(Integer, nullable=False)
    transaction_year = Column(Integer, nullable=False)
    transaction_form = Column(String, nullable=False)
    sale_reference = Column(Integer, nullable=False, default=0)
    purchase_reference = Column(Integer, nullable=False, default=0)
    credit_reference = Column(Integer, nullable=False, default=0)
    created_on = Column(Date, nullable=False, default=datetime.utcnow)
    created_by = Column(Integer, nullable=False)

class JournalDetails(Base):
    __tablename__ = 'journal_details'

    id = Column(Integer, primary_key=True, index=True)
    journal_id = Column(Integer, nullable=False)
    account_id = Column(Integer, nullable=False)
    dr_amount = Column(Float, nullable=False, default=0.00)
    cr_amount = Column(Float, default=0.00, nullable=False)
    total_amount = Column(Float, default=0.00, nullable=False)
    narrations = Column(String, nullable=False)
    folio_number = Column(String, nullable=False)
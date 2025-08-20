from sqlalchemy import Column, String, Integer, Float, DateTime
from application.config import Base
from datetime import datetime

class CreditNote(Base):
    __tablename__ = 'credit_note'

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, nullable=False)
    credit_date = Column(DateTime, nullable=False)
    credit_reasons = Column(String, nullable=False)
    credit_status = Column(String, nullable=False, default='PENDING')
    total_credit = Column(Float, nullable=False, default=0.00)
    total_vat_amount = Column(Float, nullable=False, default=0.00)
    credit_period = Column(String, nullable=False)
    reject_reasons = Column(String, nullable=True)
    created_on = Column(datetime, nullable=False)
    created_by = Column(Integer, nullable=False)
    action_on = Column(datetime, nullable=False)
    action_by = Column(Integer, nullable=False)

class CreditNoteDetail(Base):
    __tablename__ = 'credit_note_detail'

    id = Column(Integer, primary_key=True, index=True)
    header_id = Column(Integer, nullable=False)
    inventory_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False, default=0.00)
    net_price = Column(Float, nullable=False, default=0.00)
    vat_id = Column(Integer, nullable=False)
    net_vat = Column(Float, nullable=False, default=0.00)


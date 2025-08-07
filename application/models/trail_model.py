from sqlalchemy import Column, Integer, String, Float, DateTime
from application.config import Base
from datetime import datetime

class AuditTrail(Base):
    __tablename__ = 'audit_trail'

    id = Column(Integer, primary_key=True, index=True)
    module_id = Column(Integer, nullable=False)
    module_name = Column(String, nullable=False)
    action_taken = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)

class ProductMovement(Base):
    __tablename__ = 'product_movement'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, default=0, nullable=False)
    open_stock = Column(Integer, default=0, nullable=False)
    issued_qty = Column(Integer, default=0, nullable=False)
    received_qty = Column(Integer, default=0, nullable=False)
    adjusted_qty = Column(Integer, default=0, nullable=False)
    physical_qty = Column(Integer, default=0, nullable=False)
    transaction_name = Column(String, nullable=False)
    transaction_id = Column(Integer, default=0, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(Integer, nullable=False)
from sqlalchemy import Column, Integer, String, Float, DateTime
from application.config import Base
from datetime import datetime

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String, unique=True, index=True, nullable=False)
    product_name = Column(String, index=True, nullable=False)
    product_type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    buy_price = Column(Float, nullable=False)
    sell_price = Column(Float, nullable=False)
    quantity_per_unit = Column(Integer, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
    category_id = Column(Integer, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    unit_id = Column(Integer, nullable=False)
    reorder_level = Column(Integer, default=0, nullable=False)
    product_image = Column(String, nullable=True)
    non_stock_item = Column(String, default="no", nullable=False)
    tax_id = Column(Integer, nullable=False)
    warehouse_id = Column(Integer, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String, nullable=False)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, unique=True, index=True, nullable=False)
    status = Column(String, default="active", nullable=False)
    description = Column(String, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String, nullable=False)

class MeasurementUnit(Base):
    __tablename__ = 'measurement_units'

    id = Column(Integer, primary_key=True, index=True)
    unit_name = Column(String, unique=True, index=True, nullable=False)
    status = Column(String, default="active", nullable=False)
    description = Column(String, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String, nullable=False)

class Warehouse(Base):
    __tablename__ = 'warehouses'

    id = Column(Integer, primary_key=True, index=True)
    warehouse_code = Column(String, unique=True, index=True, nullable=False)
    warehouse_name = Column(String, unique=True, index=True, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, default="active", nullable=False)
    warehouse_description = Column(String, nullable=True)
    warehouse_type = Column(String, nullable=False)
    warehouse_address = Column(String, nullable=False)
    warehouse_stage = Column(String, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String, nullable=False)

class Tax(Base):
    __tablename__ = 'taxes'

    id = Column(Integer, primary_key=True, index=True)
    tax_code = Column(String, unique=True, index=True, nullable=False)
    tax_name = Column(String, unique=True, index=True, nullable=False)
    tax_rate = Column(Float, nullable=False)
    status = Column(String, default="active", nullable=False)
    description = Column(String, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String, nullable=False)
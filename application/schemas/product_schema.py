from typing import Optional
from pydantic import BaseModel
from datetime import date

class ProductCreate(BaseModel):
    product_code: str
    product_name: str
    product_type: str
    description: str
    buy_price: float
    sell_price: float
    quantity_per_unit: int
    quantity: int
    category_id: int
    supplier_id: int
    unit_id: int
    reorder_level: int
    non_stock_item: str
    tax_id: int
    warehouse_id: int
class ProductOut(BaseModel):
    id: int
    product_code: str
    product_name: str
    product_type: str
    description: str
    buy_price: float
    sell_price: float
    quantity_per_unit: int
    quantity: int
    category_id: int
    supplier_id: int
    unit_id: int
    reorder_level: int
    non_stock_item: str
    tax_id: int
    warehouse_id: int
    product_image: str
    class Config:
        orm_mode = True
class CategoryCreate(BaseModel):
    id: int
    category_name: str
    status: str
    description: str
class CategoryOut(BaseModel):
    id: int
    category_name: str
    status: str = "active"
    description: str | None = None
    class Config:
        orm_mode = True
class MeasurementUnitCreate(BaseModel):
    id: int
    unit_name: str
    status: str
    description: str
class MeasurementUnitOut(BaseModel):
    id: int
    unit_name: str
    status: str
    description: str
    class Config:
        orm_mode = True
class WarehouseCreate(BaseModel):
    id: int
    warehouse_code: str
    warehouse_name: str
    location: str
    status: str = "active"
    warehouse_description: str | None = None
    warehouse_type: str
    warehouse_address: str
    warehouse_stage: str
    quantity: int
class WarehouseOut(BaseModel):
    id: int
    warehouse_code: str
    warehouse_name: str
    location: str
    status: str = "active"
    warehouse_description: str | None = None
    warehouse_type: str
    warehouse_address: str
    warehouse_stage: str
    quantity: int = 0
    class Config:
        orm_mode = True
class TaxCreate(BaseModel):
    id: int
    tax_code: str
    tax_name: str
    tax_rate: float
    status: str
    description: str
class TaxOut(BaseModel):
    id: int
    tax_code: str
    tax_name: str
    tax_rate: float
    status: str
    description: str
    class Config:
        orm_mode = True
class RequestDetailCreate(BaseModel):
    id: int
    header_id: int
    product_id: int
    quantity: int
    unit_price: float
    net_price: float
    more_detail: str
    vat_id: int
    vat_amount: float
class RequestHeaderCreate(BaseModel):
    id: int
    request_description: str
    request_date: date
    request_status: str
    request_type: str
    details: list[RequestDetailCreate]
class RequestDetailOut(BaseModel):
    id: int
    header_id: int
    product_id: int
    quantity: int
    unit_price: float
    net_price: float
    more_detail: str
    vat_id: int
    vat_amount: float

    class Confif:
        orm_mode = True
class RequestHeaderOut(BaseModel):
    id: int
    request_description: str
    request_date: date
    request_status: str
    request_type: str
    details: list[RequestDetailCreate] = []

    class Config:
        orm_mode = True

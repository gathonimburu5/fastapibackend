from pydantic import BaseModel
from datetime import date

class ProductBase(BaseModel):
    id: int
    product_code: str
    product_name: str
    product_type: str
    description: str | None = None
    buy_price: float
    sell_price: float
    quantity_per_unit: int
    quantity: int = 0
    category_id: int
    supplier_id: int | None = None
    unit_id: int | None = None
    reorder_level: int = 0
    product_image: str | None = None
    non_stock_item: str = "no"
    tax_id: int | None = None
    warehouse_id: int | None = None

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    id: int
    category_name: str
    status: str = "active"
    description: str | None = None

class CategoryCreate(CategoryBase):
    pass
class CategoryOut(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class MeasurementUnitBase(BaseModel):
    id: int
    unit_name: str
    status: str = "active"
    description: str | None = None

class MeasurementUnitCreate(MeasurementUnitBase):
    pass
class MeasurementUnitOut(MeasurementUnitBase):
    id: int
    class Config:
        orm_mode = True

class WarehouseBase(BaseModel):
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

class WarehouseCreate(WarehouseBase):
    pass
class WarehouseOut(WarehouseBase):
    id: int
    class Config:
        orm_mode = True

class TaxBase(BaseModel):
    id: int
    tax_code: str
    tax_name: str
    tax_rate: float

class TaxCreate(TaxBase):
    pass
class TaxOut(TaxBase):
    id: int
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

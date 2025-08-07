from pydantic import BaseModel
from datetime import datetime

class AuditTrailBase(BaseModel):
    id: int
    module_id: int
    module_name: str
    action_taken: str
    user_id: str
    created_on: datetime

class AuditTrailOut(AuditTrailBase):
    id: int

    class Config:
        orm_mode = True

class ProductMovementBase(BaseModel):
    id: int
    product_id: int
    open_stock: int
    issued_qty: int
    received_qty: int
    adjusted_qty: int
    physical_qty: int
    transaction_name: str
    transaction_id: int
    created_on: datetime
    created_by: int

class ProductMovementOut(ProductMovementBase):
    id: int

    class Config:
        orm_mode = True
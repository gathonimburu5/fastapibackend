from pydantic import BaseModel
from datetime import date

class AuditTrailOut(BaseModel):
    id: int
    module_id: int
    module_name: str
    action_taken: str
    user_id: int
    created_by: str
    created_on: date
    class Config:
        orm_mode = True

    @property
    def created_on_formatted(self):
        return self.created_on.strftime("%B %d, %Y")

class ProductMovementOut(BaseModel):
    id: int
    product_id: int
    open_stock: int
    issued_qty: int
    received_qty: int
    adjusted_qty: int
    physical_qty: int
    transaction_name: str
    transaction_id: int
    created_on: date
    created_by: int
    class Config:
        orm_mode = True

class WarehouseMovementOut(BaseModel):
    id: int
    product_id: int
    warehouse_id: int
    open_stock: int
    issued_qty: int
    received_qty: int
    adjusted_qty: int
    physical_qty: int
    transfer_qty: int
    transaction_name: str
    transaction_id: int
    created_on: date
    created_by: int
    class Config:
        orm_mode = True
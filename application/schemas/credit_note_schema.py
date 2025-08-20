from pydantic import BaseModel
from datetime import date

class CreditNoteDetailCreate(BaseModel):
    header_id: int
    inventory_id: int
    quantity: int
    unit_price: float
    net_price: float
    vat_id: int
    net_vat: float

class CreditNoteCreate(BaseModel):
    invoice_id: int
    credit_date: date
    credit_reasons: str
    total_credit: float
    total_vat_amount: float
    credit_period: str
    details: list[CreditNoteDetailCreate]

class CreditNoteDetailOut(BaseModel):
    id: int
    header_id: int
    inventory_id: int
    quantity: int
    unit_price: float
    net_price: float
    vat_id: int
    net_vat: float

    class Config:
        orm_mode = True

class CreditNoteOut(BaseModel):
    id: int
    invoice_id: int
    credit_date: date
    credit_reasons: str
    total_credit: float
    total_vat_amount: float
    credit_period: str
    reject_reasons: str
    details: list[CreditNoteDetailCreate] = []

    class Config:
        orm_mode = True
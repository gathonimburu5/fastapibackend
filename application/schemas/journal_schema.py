from pydantic import BaseModel
from datetime import datetime

class JournalDetailCreate(BaseModel):
    journal_id: int
    account_id: int
    dr_amount: float
    cr_amount: float
    total_amount: float
    narrations: str
    folio_number: str
class JournalHeaderCreate(BaseModel):
    journal_description: str
    journal_date: datetime
    transaction_period: int
    transaction_year: int
    transaction_form: str
    sale_reference: int
    purchase_reference: int
    credit_reference: int
    details: list[JournalDetailCreate]
class JournalDetailOut(BaseModel):
    id: int
    journal_id: int
    account_id: int
    dr_amount: float
    cr_amount: float
    total_amount: float
    narrations: str
    folio_number: str

    class Config:
        orm_mode = True
class JournalHeaderOut(BaseModel):
    id: int
    journal_description: str
    journal_date: datetime
    transaction_period: int
    transaction_year: int
    transaction_form: str
    sale_reference: int
    purchase_reference: int
    credit_reference: int
    details: list[JournalDetailCreate] = []

    class Config:
        orm_mode = True

from datetime import date
from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from application.schemas.employee_schema import CustomerCreate, CustomerOut
from application.services.customer_service import CustomerService
from application.config import get_db
from application.utility.token import get_current_user
from application.schemas.user_schema import UserToken


customer_router = APIRouter()
customerService = CustomerService()

@customer_router.get("/customers", response_model=list[CustomerOut])
def get_customers(db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    return customerService.getAllCustomers(db)

@customer_router.post("/customers", response_model=CustomerOut)
def create_customer(
    customer_name: str = Form(...),
    email_address: str = Form(...),
    phone_number: str = Form(...),
    postal_address: str = Form(...),
    physical_address: str = Form(...),
    date_of_birth: date = Form(...),
    date_of_registration: date = Form(...),
    vat_pin: str = Form(...),
    credit_limit: float = Form(...),
    sales_rep_id: int = Form(...),
    status: str = Form(...),
    opening_balance: float = Form(...),
    opening_balance_date: date = Form(...),
    opening_balance_rate: float = Form(...),
    currency_id: int = Form(...),
    bs_file: UploadFile = File(...),
    cr12_file: UploadFile = File(...),
    permit_file: UploadFile = File(...),
    db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    customer_obj = CustomerCreate(
        customer_name=customer_name,
        email_address= email_address,
        phone_number= phone_number,
        postal_address= postal_address,
        physical_address= physical_address,
        date_of_birth=date_of_birth,
        date_of_registration=date_of_registration,
        vat_pin=vat_pin,
        credit_limit=credit_limit,
        sales_rep_id=sales_rep_id,
        opening_balance=opening_balance,
        opening_balance_date=opening_balance_date,
        opening_balance_rate=opening_balance_rate,
        currency_id=currency_id
    )
    customerService.createCustomerService(customer_obj, bs_file, cr12_file, permit_file, db, current_user)
    return JSONResponse(content={"message": "successfully created customer record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@customer_router.get("/customers/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    customer_record = customerService.getCustomerById(customer_id, db)
    if not customer_record:
        return JSONResponse(content={"error": "customer record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return customer_record

@customer_router.put("/customers/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    customer_record = customerService.updateCustomerService(customer_id, customer, db, current_user)
    if not customer_record:
        return JSONResponse(content={"error": "customer record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated customer record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

# @customer_router.delete("/customers/{customer_id}")
# def delete_customer(customer_id: int, db: Session = Depends(get_db)):
#     result = customerService.deleteCustomerService(customer_id, db)
#     if not result:
#         return JSONResponse(content={"error": "customer record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
#     return JSONResponse(content={"message": "successfully deleted customer record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)
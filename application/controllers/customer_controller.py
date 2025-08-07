from fastapi import APIRouter, Depends, status
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
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    customerService.createCustomerService(customer, db, current_user)
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
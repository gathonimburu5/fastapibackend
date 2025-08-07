from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from application.config import SessionLocal
from application.schemas.employee_schema import EmployeeCreate, EmployeeOut
from application.services.employee_service import EmployeeService
from fastapi.responses import JSONResponse
from application.config import get_db
from application.utility.token import get_current_user
from application.schemas.user_schema import UserToken

employee_router = APIRouter()
employeeService = EmployeeService()

@employee_router.get("/employees", response_model=list[EmployeeOut])
def get_employees(db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    return employeeService.getAllEmployee(db)

@employee_router.post("/employees", response_model=EmployeeOut)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    employeeService.createEmployeeService(employee, db, current_user)
    return JSONResponse(content={"message": "successfully created employee record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@employee_router.get("/employees/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: int, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    employee_record = employeeService.getEmployeeById(employee_id, db)
    if not employee_record:
        return JSONResponse(content={"error": "employee record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return employee_record

@employee_router.put("/employees/{employee_id}", response_model=EmployeeOut)
def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    employee_record = employeeService.updateEmployeeService(employee_id, employee, db, current_user)
    if not employee_record:
        return JSONResponse(content={"error": "employee record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated employee record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@employee_router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    result = employeeService.deleteEmployeeService(employee_id, db)
    if not result:
        JSONResponse(content={"error": "employee record not found", "code": status.HTTP_404_NOT_FOUND}, status_code = status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully deleted employee record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)
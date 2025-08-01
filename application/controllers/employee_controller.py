from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from application.config import SessionLocal
from application.models.employee_model import Employee
from application.schemas.employee_schema import EmployeeCreate, EmployeeOut
from application.services.employee_service import createEmployeeService, getAllEmployee, getEmployeeById, updateEmployeeService, deleteEmployeeService
from fastapi.responses import JSONResponse

employee_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@employee_router.get("/employees", response_model=list[EmployeeOut])
async def get_employees(db: Session = Depends(get_db)):
    return await getAllEmployee(db)

@employee_router.post("/employees", response_model=EmployeeOut)
async def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    await createEmployeeService(employee, db)
    return JSONResponse(content={"message": "successfully created employee record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@employee_router.get("/employees/{employee_id}", response_model=EmployeeOut)
async def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee_record = await getEmployeeById(employee_id, db)
    if not employee_record:
        return JSONResponse(content={"error": "employee record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return employee_record

@employee_router.put("/employees/{employee_id}", response_model=EmployeeOut)
async def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    employee_record = await updateEmployeeService(employee_id, employee, db)
    if not employee_record:
        return JSONResponse(content={"error": "employee record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated employee record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@employee_router.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    result = await deleteEmployeeService(employee_id, db)
    if not result:
        JSONResponse(content={"error": "employee record not found", "code": status.HTTP_404_NOT_FOUND}, status_code = status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully deleted employee record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)
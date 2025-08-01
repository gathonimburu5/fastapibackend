from sqlalchemy.orm import Session
from application.models.employee_model import Employee
from application.schemas.employee_schema import EmployeeCreate

async def createEmployeeService(employee: EmployeeCreate, db: Session):
    new_employee = Employee(
        employee_name=employee.employee_name,
        email_address=employee.email_address,
        id_number=employee.id_number,
        phone_number=employee.phone_number,
        department=employee.department,
        postal_address=employee.postal_address,
        date_of_birth=employee.date_of_birth,
        date_of_joining=employee.date_of_joining,
        physical_address=employee.physical_address,
        designation=employee.designation,
        salary=employee.salary
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

async def getAllEmployee(db: Session):
    return db.query(Employee).all()

async def getEmployeeById(employee_id: int, db: Session):
    employee_record = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee_record:
        return employee_record
    return None

async def updateEmployeeService(employee_id: int, employee: EmployeeCreate, db: Session):
    employee_record = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee_record:
        return None
    employee_record.employee_name = employee.employee_name
    employee_record.email_address = employee.email_address
    employee_record.id_number = employee.id_number
    employee_record.phone_number = employee.phone_number
    employee_record.department = employee.department
    employee_record.postal_address = employee.postal_address
    employee_record.date_of_birth = employee.date_of_birth
    employee_record.date_of_joining = employee.date_of_joining
    employee_record.physical_address = employee.physical_address
    employee_record.designation = employee.designation
    employee_record.salary = employee.salary
    db.commit()
    db.refresh(employee_record)
    return employee_record

async def deleteEmployeeService(employee_id: int, db: Session):
    employee_record = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee_record:
        return None
    db.delete(employee_record)
    db.commit()
    return employee_record


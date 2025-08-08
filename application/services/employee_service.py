from sqlalchemy.orm import Session
from application.models.employee_model import Employee
from application.schemas.employee_schema import EmployeeCreate
from application.models.trail_model import AuditTrail

class EmployeeService:
    def createEmployeeService(self, employee: EmployeeCreate, db: Session, current_user):
        try:
            user_id = current_user.id
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
                salary=employee.salary,
                created_by=user_id
            )
            db.add(new_employee)
            db.flush()

            # create audit trail
            create_trail = AuditTrail(
                module_id = new_employee.id,
                module_name = "createEmployee",
                action_taken = "CREATING EMPLOYEE RECORD",
                user_id = user_id
            )
            db.add(create_trail)

            db.commit()
            db.refresh(new_employee)
            return new_employee
        except Exception as e:
            db.rollback()
            return f"an error occurred: {str(e)}"

    def getAllEmployee(self, db: Session):
        return db.query(Employee).all()

    def getEmployeeById(self, employee_id: int, db: Session):
        employee_record = db.query(Employee).filter(Employee.id == employee_id).first()
        if employee_record:
            return employee_record
        return None

    def updateEmployeeService(self, employee_id: int, employee: EmployeeCreate, db: Session, current_user):
        try:
            userId = current_user.id
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

            # create audit trail
            create_trail = AuditTrail(
                module_id = employee_record.id,
                module_name = "updateEmployee",
                action_taken = "UPDATING EMPLOYEE RECORD",
                user_id = userId
            )
            db.add(create_trail)

            db.commit()
            db.refresh(employee_record)
            return employee_record
        except Exception as e:
            db.rollback()
            return f"an error occurred: {str(e)}"

    def deleteEmployeeService(self, employee_id: int, db: Session):
        employee_record = db.query(Employee).filter(Employee.id == employee_id).first()
        if not employee_record:
            return None
        db.delete(employee_record)
        db.commit()
        return employee_record




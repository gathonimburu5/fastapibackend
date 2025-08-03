from sqlalchemy.orm import Session
from application.models.employee_model import Employee, Customer
from application.schemas.employee_schema import EmployeeCreate, CustomerCreate

class EmployeeService:
    def createEmployeeService(self, employee: EmployeeCreate, db: Session, current_user):
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
        db.commit()
        db.refresh(new_employee)
        return new_employee

    def getAllEmployee(self, db: Session, current_user):
        return db.query(Employee).all()

    def getEmployeeById(self, employee_id: int, db: Session):
        employee_record = db.query(Employee).filter(Employee.id == employee_id).first()
        if employee_record:
            return employee_record
        return None

    def updateEmployeeService(self, employee_id: int, employee: EmployeeCreate, db: Session):
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

    def deleteEmployeeService(self, employee_id: int, db: Session):
        employee_record = db.query(Employee).filter(Employee.id == employee_id).first()
        if not employee_record:
            return None
        db.delete(employee_record)
        db.commit()
        return employee_record

    def getAllCustomers(self, db: Session):
        return db.query(Customer).all()

    def createCustomerService(self, customer: CustomerCreate, db: Session):
        new_customer = Customer(
            customer_name=customer.customer_name,
            email_address=customer.email_address,
            phone_number=customer.phone_number,
            postal_address=customer.postal_address,
            physical_address=customer.physical_address,
            date_of_birth=customer.date_of_birth,
            date_of_registration=customer.date_of_registration,
            vat_pin=customer.vat_pin,
            credit_limit=customer.credit_limit,
            sales_rep_id=customer.sales_rep_id,
            status=customer.status,
            opening_balance=customer.opening_balance,
            opening_balance_date=customer.opening_balance_date,
            opening_balance_rate=customer.opening_balance_rate,
            currency_id=customer.currency_id
        )
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return new_customer

    def getCustomerById(self, customer_id: int, db: Session):
        customer_record = db.query(Customer).filter(Customer.id == customer_id).first()
        if customer_record:
            return customer_record
        return None

    def updateCustomerService(self, customer_id: int, customer: CustomerCreate, db: Session):
        customer_record = db.query(Customer).filter(Customer.id == customer_id).first()
        if not customer_record:
            return None
        customer_record.customer_name = customer.customer_name
        customer_record.email_address = customer.email_address
        customer_record.phone_number = customer.phone_number
        customer_record.postal_address = customer.postal_address
        customer_record.physical_address = customer.physical_address
        customer_record.date_of_birth = customer.date_of_birth
        customer_record.date_of_registration = customer.date_of_registration
        customer_record.vat_pin = customer.vat_pin
        customer_record.credit_limit = customer.credit_limit
        customer_record.sales_rep_id = customer.sales_rep_id
        customer_record.status = customer.status
        customer_record.opening_balance = customer.opening_balance
        customer_record.opening_balance_date = customer.opening_balance_date
        customer_record.opening_balance_rate = customer.opening_balance_rate
        customer_record.currency_id = customer.currency_id
        db.commit()
        db.refresh(customer_record)
        return customer_record

    def deleteCustomerService(self, customer_id: int, db: Session):
        customer_record = db.query(Customer).filter(Customer.id == customer_id).first()
        if not customer_record:
            return None
        db.delete(customer_record)
        db.commit()
        return customer_record


from sqlalchemy.orm import Session
from application.models.employee_model import Customer
from application.schemas.employee_schema import CustomerCreate
from application.models.trail_model import AuditTrail
from application.utility.files import saveFiles
from fastapi import UploadFile

class CustomerService:
    async def createCustomerService(self, customer: CustomerCreate, bsCertificate: UploadFile, cr12Certificate: UploadFile, bsPermit: UploadFile, db: Session, current_user):
        try:
            user_id = current_user.id
            bs_file = await saveFiles(bsCertificate, "CustomerFiles")
            cr12_file = await saveFiles(cr12Certificate, "CustomerFiles")
            permit_file = await saveFiles(bsPermit, "CustomerFiles")
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
                opening_balance=customer.opening_balance,
                opening_balance_date=customer.opening_balance_date,
                opening_balance_rate=customer.opening_balance_rate,
                currency_id=customer.currency_id,
                created_by=user_id,
                business_certificate = bs_file,
                cr12_certificate = cr12_file,
                business_permit = permit_file
            )
            db.add(new_customer)
            db.flush()

            # create audit trail
            create_trail = AuditTrail(
                module_id = new_customer.id,
                module_name = "CreateCustomer",
                action_taken = "CREATING CUSTOMER RECORD",
                user_id = user_id
            )
            db.add(create_trail)

            db.commit()
            db.refresh(new_customer)
            return new_customer
        except Exception as e:
            db.rollback()
            return f"an error occurred: {str(e)}"

    def getAllCustomers(self, db: Session):
        return db.query(Customer).all()

    def getCustomerById(self, customer_id: int, db: Session):
        customer_record = db.query(Customer).filter(Customer.id == customer_id).first()
        if customer_record:
            return customer_record
        return None

    def updateCustomerService(self, customer_id: int, customer: CustomerCreate, db: Session, current_user):
        try:
            user_id = current_user.id
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
            customer_record.opening_balance = customer.opening_balance
            customer_record.opening_balance_date = customer.opening_balance_date
            customer_record.opening_balance_rate = customer.opening_balance_rate
            customer_record.currency_id = customer.currency_id

            # create audit trail
            create_trail = AuditTrail(
                module_id = customer_record.id,
                module_name = "UpdateCustomer",
                action_taken = "UPDATING CUSTOMER RECORD",
                user_id = user_id
            )
            db.add(create_trail)

            db.commit()
            db.refresh(customer_record)
            return customer_record
        except Exception as e:
            db.rollback()
            return f"an error occurred: {str(e)}"

    def deleteCustomerService(self, customer_id: int, db: Session):
        customer_record = db.query(Customer).filter(Customer.id == customer_id).first()
        if not customer_record:
            return None
        db.delete(customer_record)
        db.commit()
        return customer_record
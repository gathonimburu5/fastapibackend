from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from application.config import Base, engine
from application.utility.token import get_current_user

# Import all models to register them with Base
from application.models.user_model import Signup
from application.models.employee_model import Employee, Customer
from application.models.product_model import Product, Category, MeasurementUnit, Warehouse, Tax, RequestHeader, RequestDetail
from application.models.journal_model import JournalHeader, JournalDetails
from application.models.credit_note_model import CreditNote, CreditNoteDetail
from application.models.trail_model import AuditTrail, ProductMovement, WarehouseMovement

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Backend API",
    description="Backend API for managing employee data",
    version="1.0.0",
    docs_url="/"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

from application.controllers.employee_controller import employee_router
app.include_router(employee_router, prefix="/api", tags=["Employees"], dependencies=[Depends(get_current_user)])

from application.controllers.customer_controller import customer_router
app.include_router(customer_router, prefix="/api", tags=["Customers"], dependencies=[Depends(get_current_user)])

from application.controllers.product_controller import product_router
app.include_router(product_router, prefix="/api", tags=["Products"], dependencies=[Depends(get_current_user)])

from application.controllers.authentication_controller import authentication_router
app.include_router(authentication_router, prefix="/api", tags=["Authentication"])

from application.controllers.trail_controller import trail_router
app.include_router(trail_router, prefix="/api", tags=["AuditTrails"], dependencies=[Depends(get_current_user)])
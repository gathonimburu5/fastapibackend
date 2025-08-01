from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from application.config import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Backend API",
    description="Backend API for managing employee data",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

from application.controllers.employee_controller import employee_router
app.include_router(employee_router, prefix="/api", tags=["Employees"])

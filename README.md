# FastAPI Backend Application

A robust backend application built with FastAPI framework providing RESTful APIs for product, employee, and customer management with authentication.

## Features

- User Authentication with JWT tokens
- Product Management
  - CRUD operations for products
  - Category management
  - Measurement units
  - Warehouse management
  - Tax management
  - Request management
- Employee Management
  - Employee records
  - Employee details
- Customer Management
  - Customer records and profiles
- Security
  - Password hashing with bcrypt
  - JWT token authentication
  - Role-based access control

## Project Structure

```
application/
├── config.py           # Database and app configuration
├── main.py            # FastAPI application entry point
├── controllers/       # API route handlers
│   ├── authentication_controller.py
│   ├── customer_controller.py
│   ├── employee_controller.py
│   └── product_controller.py
├── models/           # Database models
│   ├── employee_model.py
│   ├── product_model.py
│   └── user_model.py
├── schemas/          # Pydantic models for request/response
│   ├── employee_schema.py
│   ├── product_schema.py
│   └── user_schema.py
├── services/         # Business logic
│   ├── authentication_service.py
│   ├── customer_service.py
│   ├── employee_service.py
│   └── product_service.py
└── utility/          # Helper functions
    ├── security.py
    └── token.py
```

## Prerequisites

- Python 3.12+
- PostgreSQL database
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gathonimburu5/fastapibackend.git
cd fastapibackend
```

2. Create and activate virtual environment:
```bash
python -m venv env
# For Windows
.\env\Scripts\activate
# For Unix or MacOS
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
- Create a PostgreSQL database
- Update the database configuration in `application/config.py`

5. Run the application:
```bash
python run.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Authentication
- POST `/auth/login` - User login
- POST `/auth/register` - User registration

### Products
- GET `/products` - List all products
- POST `/products` - Create new product
- GET `/products/{product_id}` - Get product details
- PUT `/products/{product_id}` - Update product
- GET `/categories` - List all categories
- POST `/categories` - Create new category
- GET `/measurement_units` - List measurement units
- GET `/warehouses` - List warehouses
- GET `/taxes` - List taxes
- GET `/requests` - List requests

### Employees
- GET `/employees` - List all employees
- POST `/employees` - Create new employee
- GET `/employees/{employee_id}` - Get employee details
- PUT `/employees/{employee_id}` - Update employee

### Customers
- GET `/customers` - List all customers
- POST `/customers` - Create new customer
- GET `/customers/{customer_id}` - Get customer details
- PUT `/customers/{customer_id}` - Update customer

## Security

The application implements several security measures:
- Password hashing using bcrypt
- JWT token-based authentication
- Role-based access control for endpoints
- Database connection security

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License

## Author

gathonimburu5
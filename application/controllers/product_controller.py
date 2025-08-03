from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from application.config import SessionLocal
from fastapi.responses import JSONResponse
from application.schemas.product_schema import ProductCreate, ProductOut, CategoryCreate, CategoryOut, MeasurementUnitCreate, MeasurementUnitOut, WarehouseCreate, WarehouseOut, TaxCreate, TaxOut
from application.services.product_service import ProductService
from application.config import get_db
from application.utility.token import get_current_user

product_router = APIRouter()
productService = ProductService()

@product_router.get("/products", response_model=list[ProductOut], dependencies=[Depends(get_current_user)])
def get_products(db: Session = Depends(get_db)):
    return productService.getAllProductRecords(db)

@product_router.post("/products", response_model=ProductOut, dependencies=[Depends(get_current_user)])
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    productService.createProductRecord(product, db)
    return JSONResponse(content={"message": "successfully created product record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/products/{product_id}", response_model=ProductOut, dependencies=[Depends(get_current_user)])
def get_product(product_id: int, db: Session = Depends(get_db)):
    product_record = productService.getProductById(product_id, db)
    if not product_record:
        return JSONResponse(content={"error": "product record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return product_record

@product_router.put("/products/{product_id}", response_model=ProductOut, dependencies=[Depends(get_current_user)])
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    product_record = productService.updateProductRecord(product_id, product, db)
    if not product_record:
        return JSONResponse(content={"error": "product record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated product record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@product_router.get("/categories", response_model=list[CategoryOut], dependencies=[Depends(get_current_user)])
def get_categories(db: Session = Depends(get_db)):
    return productService.getAllCategories(db)

@product_router.post("/categories", response_model=CategoryOut, dependencies=[Depends(get_current_user)])
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    productService.createCategory(category, db)
    return JSONResponse(content={"message": "successfully created category record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/categories/{category_id}", response_model=CategoryOut, dependencies=[Depends(get_current_user)])
def get_category(category_id: int, db: Session = Depends(get_db)):
    category_record = productService.getCategoryById(category_id, db)
    if not category_record:
        return JSONResponse(content={"error": "category record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return category_record

@product_router.put("/categories/{category_id}", response_model=CategoryOut, dependencies=[Depends(get_current_user)])
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    category_record = productService.updateCategory(category_id, category, db)
    if not category_record:
        return JSONResponse(content={"error": "category record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated category record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@product_router.get("/measurement_units", response_model=list[MeasurementUnitOut], dependencies=[Depends(get_current_user)])
def get_measurement_units(db: Session = Depends(get_db)):
    return productService.getAllMeasurementUnits(db)

@product_router.post("/measurement_units", response_model=MeasurementUnitOut, dependencies=[Depends(get_current_user)])
def create_measurement_unit(unit: MeasurementUnitCreate, db: Session = Depends(get_db)):
    productService.createMeasurementUnit(unit, db)
    return JSONResponse(content={"message": "successfully created measurement unit record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/measurement_units/{unit_id}", response_model=MeasurementUnitOut, dependencies=[Depends(get_current_user)])
def get_measurement_unit(unit_id: int, db: Session = Depends(get_db)):
    unit_record = productService.getMeasurementUnitById(unit_id, db)
    if not unit_record:
        return JSONResponse(content={"error": "measurement unit record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return unit_record

@product_router.put("/measurement_units/{unit_id}", response_model=MeasurementUnitOut, dependencies=[Depends(get_current_user)])
def update_measurement_unit(unit_id: int, unit: MeasurementUnitCreate, db: Session = Depends(get_db)):
    unit_record = productService.updateMeasurementUnit(unit_id, unit, db)
    if not unit_record:
        return JSONResponse(content={"error": "measurement unit record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated measurement unit record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@product_router.get("/warehouses", response_model=list[WarehouseOut], dependencies=[Depends(get_current_user)])
def get_warehouses(db: Session = Depends(get_db)):
    return productService.getAllWarehouses(db)

@product_router.post("/warehouses", response_model=WarehouseOut, dependencies=[Depends(get_current_user)])
def create_warehouse(warehouse: WarehouseCreate, db: Session = Depends(get_db)):
    productService.createWarehouse(warehouse, db)
    return JSONResponse(content={"message": "successfully created warehouse record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/warehouses/{warehouse_id}", response_model=WarehouseOut, dependencies=[Depends(get_current_user)])
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    warehouse_record = productService.getWarehouseById(warehouse_id, db)
    if not warehouse_record:
        return JSONResponse(content={"error": "warehouse record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return warehouse_record

@product_router.put("/warehouses/{warehouse_id}", response_model=WarehouseOut, dependencies=[Depends(get_current_user)])
def update_warehouse(warehouse_id: int, warehouse: WarehouseCreate, db: Session = Depends(get_db)):
    warehouse_record = productService.updateWarehouse(warehouse_id, warehouse, db)
    if not warehouse_record:
        return JSONResponse(content={"error": "warehouse record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated warehouse record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@product_router.get("/taxes", response_model=list[TaxOut], dependencies=[Depends(get_current_user)])
def get_taxes(db: Session = Depends(get_db)):
    return productService.getAllTaxes(db)

@product_router.post("/taxes", response_model=TaxOut, dependencies=[Depends(get_current_user)])
def create_tax(tax: TaxCreate, db: Session = Depends(get_db)):
    productService.createTax(tax, db)
    return JSONResponse(content={"message": "successfully created tax record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/taxes/{tax_id}", response_model=TaxOut, dependencies=[Depends(get_current_user)])
def get_tax(tax_id: int, db: Session = Depends(get_db)):
    tax_record = productService.getTaxById(tax_id, db)
    if not tax_record:
        return JSONResponse(content={"error": "tax record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return tax_record

@product_router.put("/taxes/{tax_id}", response_model=TaxOut, dependencies=[Depends(get_current_user)])
def update_tax(tax_id: int, tax: TaxCreate, db: Session = Depends(get_db)):
    tax_record = productService.updateTax(tax_id, tax, db)
    if not tax_record:
        return JSONResponse(content={"error": "tax record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated tax record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)


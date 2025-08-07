from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from application.config import SessionLocal
from fastapi.responses import JSONResponse
from application.schemas.product_schema import ProductCreate, ProductOut, CategoryCreate, CategoryOut, MeasurementUnitCreate, MeasurementUnitOut, WarehouseCreate, WarehouseOut, TaxCreate, TaxOut, RequestHeaderCreate, RequestHeaderOut
from application.services.product_service import ProductService
from application.config import get_db
from application.utility.token import get_current_user
from application.schemas.user_schema import UserToken

product_router = APIRouter()
productService = ProductService()

@product_router.get("/products", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    return productService.getAllProductRecords(db)

@product_router.post("/products", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    productService.createProductRecord(product, db, current_user)
    return JSONResponse(content={"message": "successfully created product record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    product_record = productService.getProductById(product_id, db)
    if not product_record:
        return JSONResponse(content={"error": "product record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return product_record

@product_router.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    product_record = productService.updateProductRecord(product_id, product, db)
    if not product_record:
        return JSONResponse(content={"error": "product record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated product record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@product_router.get("/categories", response_model=list[CategoryOut])
def get_categories(db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    return productService.getAllCategories(db)

@product_router.post("/categories", response_model=CategoryOut)
def create_category(category: CategoryCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    productService.createCategory(category, db, current_user)
    return JSONResponse(content={"message": "successfully created category record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/categories/{category_id}", response_model=CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    category_record = productService.getCategoryById(category_id, db)
    if not category_record:
        return JSONResponse(content={"error": "category record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return category_record

@product_router.put("/categories/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    category_record = productService.updateCategory(category_id, category, db)
    if not category_record:
        return JSONResponse(content={"error": "category record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated category record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@product_router.get("/measurement_units", response_model=list[MeasurementUnitOut])
def get_measurement_units(db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    return productService.getAllMeasurementUnits(db)

@product_router.post("/measurement_units", response_model=MeasurementUnitOut)
def create_measurement_unit(unit: MeasurementUnitCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    productService.createMeasurementUnit(unit, db, current_user)
    return JSONResponse(content={"message": "successfully created measurement unit record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/measurement_units/{unit_id}", response_model=MeasurementUnitOut)
def get_measurement_unit(unit_id: int, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    unit_record = productService.getMeasurementUnitById(unit_id, db)
    if not unit_record:
        return JSONResponse(content={"error": "measurement unit record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return unit_record

@product_router.put("/measurement_units/{unit_id}", response_model=MeasurementUnitOut)
def update_measurement_unit(unit_id: int, unit: MeasurementUnitCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    unit_record = productService.updateMeasurementUnit(unit_id, unit, db)
    if not unit_record:
        return JSONResponse(content={"error": "measurement unit record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated measurement unit record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@product_router.get("/warehouses", response_model=list[WarehouseOut])
def get_warehouses(db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    return productService.getAllWarehouses(db)

@product_router.post("/warehouses", response_model=WarehouseOut)
def create_warehouse(warehouse: WarehouseCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    productService.createWarehouse(warehouse, db, current_user)
    return JSONResponse(content={"message": "successfully created warehouse record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/warehouses/{warehouse_id}", response_model=WarehouseOut)
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    warehouse_record = productService.getWarehouseById(warehouse_id, db)
    if not warehouse_record:
        return JSONResponse(content={"error": "warehouse record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return warehouse_record

@product_router.put("/warehouses/{warehouse_id}", response_model=WarehouseOut)
def update_warehouse(warehouse_id: int, warehouse: WarehouseCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    warehouse_record = productService.updateWarehouse(warehouse_id, warehouse, db)
    if not warehouse_record:
        return JSONResponse(content={"error": "warehouse record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated warehouse record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@product_router.get("/taxes", response_model=list[TaxOut])
def get_taxes(db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    return productService.getAllTaxes(db)

@product_router.post("/taxes", response_model=TaxOut)
def create_tax(tax: TaxCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    productService.createTax(tax, db, current_user)
    return JSONResponse(content={"message": "successfully created tax record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/taxes/{tax_id}", response_model=TaxOut)
def get_tax(tax_id: int, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    tax_record = productService.getTaxById(tax_id, db)
    if not tax_record:
        return JSONResponse(content={"error": "tax record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return tax_record

@product_router.put("/taxes/{tax_id}", response_model=TaxOut)
def update_tax(tax_id: int, tax: TaxCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    tax_record = productService.updateTax(tax_id, tax, db)
    if not tax_record:
        return JSONResponse(content={"error": "tax record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "successfully updated tax record", "code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

@product_router.get("/requests", response_model=list[RequestHeaderOut])
def get_requests(db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    return productService.getAllRequest(db)

@product_router.post("/requests", response_model=RequestHeaderOut)
def create_request(request: RequestHeaderCreate, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    productService.createRequest(request, db, current_user)
    return JSONResponse(content={"message": "successfully created request's record", "code": status.HTTP_201_CREATED}, status_code=status.HTTP_201_CREATED)

@product_router.get("/requests/{request_id}", response_model=RequestHeaderOut)
def get_request(request_id: int, db: Session = Depends(get_db), current_user: UserToken = Depends(get_current_user)):
    request_result = productService.getRequestPerId(request_id, db)
    if not request_result:
        return JSONResponse(content={"error": "request record not found", "code": status.HTTP_404_NOT_FOUND}, status_code=status.HTTP_404_NOT_FOUND)
    return request_result

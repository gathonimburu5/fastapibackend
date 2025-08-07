from sqlalchemy.orm import Session
from application.models.product_model import Product, Category, MeasurementUnit, Warehouse, Tax, RequestHeader, RequestDetail
from application.schemas.product_schema import ProductCreate, CategoryCreate, MeasurementUnitCreate, WarehouseCreate, TaxCreate, RequestHeaderCreate
from application.models.trail_model import AuditTrail, ProductMovement

class ProductService:
    def getAllProductRecords(self, db: Session):
        return db.query(Product).all()

    def createProductRecord(self, product: ProductCreate, db: Session, current_user):
        user_id = current_user.id
        new_product = Product(
            product_code=product.product_code,
            product_name=product.product_name,
            product_type=product.product_type,
            description=product.description,
            buy_price=product.buy_price,
            sell_price=product.sell_price,
            quantity_per_unit=product.quantity_per_unit,
            quantity=product.quantity,
            category_id=product.category_id,
            supplier_id=product.supplier_id,
            unit_id=product.unit_id,
            reoder_level=product.reorder_level,
            product_image=product.product_image,
            nonstock_item=product.non_stock_item,
            tax_id=product.tax_id,
            warehouse_id=product.warehouse_id,
            created_by = user_id
        )
        db.add(new_product)
        db.flush(new_product)
        db.commit()
        db.refresh(new_product)

        # create product movement
        openQ = new_product.quantity
        issueQ = 0
        receiveQ = 0
        adjQ = 0
        phyQ = (openQ + issueQ + receiveQ + adjQ)
        product_movement = ProductMovement(
            product_id = new_product.id,
            open_stock = openQ,
            issued_qty = issueQ,
            received_qty = receiveQ,
            adjusted_qty = adjQ,
            physical_qty = phyQ,
            transaction_name = "",
            created_by = user_id
        )
        db.add(product_movement)

        # create audit trail
        create_trail = AuditTrail(
            module_id = new_product.id,
            module_name = "PostProductRecord",
            action_taken = "CREATING PRODUCT RECORD",
            user_id = user_id
        )
        db.add(create_trail)
        db.commit()
        return new_product

    def getProductById(self, product_id: int, db: Session):
        product_record = db.query(Product).filter(Product.id == product_id).first()
        if product_record:
            return product_record
        return None

    def updateProductRecord(self, product_id: int, product: ProductCreate, db: Session):
        product_record = db.query(Product).filter(Product.id == product_id).first()
        if not product_record:
            return None
        product_record.product_code = product.product_code
        product_record.product_name = product.product_name
        product_record.product_type = product.product_type
        product_record.description = product.description
        product_record.buy_price = product.buy_price
        product_record.sell_price = product.sell_price
        product_record.quantity_per_unit = product.quantity_per_unit
        product_record.quantity = product.quantity
        product_record.category_id = product.category_id
        product_record.supplier_id = product.supplier_id
        product_record.unit_id = product.unit_id
        product_record.reorder_level = product.reorder_level
        product_record.product_image = product.product_image
        product_record.non_stock_item = product.non_stock_item
        product_record.tax_id = product.tax_id
        product_record.warehouse_id = product.warehouse_id
        db.commit()
        db.refresh(product_record)
        return product_record

    def deleteProductRecord(self, product_id: int, db: Session):
        product_record = db.query(Product).filter(Product.id == product_id).first()
        if not product_record:
            return None
        db.delete(product_record)
        db.commit()
        return product_record

    def getAllCategories(self, db: Session):
        return db.query(Category).all()

    def createCategory(self, category: CategoryCreate, db: Session, current_user):
        user_id = current_user.id
        new_category = Category(
            category_name=category.category_name,
            status=category.status,
            description=category.description,
            created_by = user_id
        )
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category

    def getCategoryById(self, category_id: int, db: Session):
        category_record = db.query(Category).filter(Category.id == category_id).first()
        if category_record:
            return category_record
        return None

    def updateCategory(self, category_id: int, category: CategoryCreate, db: Session):
        category_record = db.query(Category).filter(Category.id == category_id).first()
        if not category_record:
            return None
        category_record.category_name = category.category_name
        category_record.status = category.status
        category_record.description = category.description
        db.commit()
        db.refresh(category_record)
        return category_record

    def deleteCategory(self, category_id: int, db: Session):
        category_record = db.query(Category).filter(Category.id == category_id).first()
        if not category_record:
            return None
        db.delete(category_record)
        db.commit()
        return category_record

    def getAllMeasurementUnits(self, db: Session):
        return db.query(MeasurementUnit).all()

    def createMeasurementUnit(self, unit: MeasurementUnitCreate, db: Session, current_user):
        user_id = current_user.id
        new_unit = MeasurementUnit(
            unit_name=unit.unit_name,
            status=unit.status,
            description=unit.description,
            created_by = user_id
        )
        db.add(new_unit)
        db.commit()
        db.refresh(new_unit)
        return new_unit

    def getMeasurementUnitById(self, unit_id: int, db: Session):
        unit_record = db.query(MeasurementUnit).filter(MeasurementUnit.id == unit_id).first()
        if unit_record:
            return unit_record
        return None

    def updateMeasurementUnit(self, unit_id: int, unit: MeasurementUnitCreate, db: Session):
        unit_record = db.query(MeasurementUnit).filter(MeasurementUnit.id == unit_id).first()
        if not unit_record:
            return None
        unit_record.unit_name = unit.unit_name
        unit_record.status = unit.status
        unit_record.description = unit.description
        db.commit()
        db.refresh(unit_record)
        return unit_record

    def deleteMeasurementUnit(self, unit_id: int, db: Session):
        unit_record = db.query(MeasurementUnit).filter(MeasurementUnit.id == unit_id).first()
        if not unit_record:
            return None
        db.delete(unit_record)
        db.commit()
        return unit_record

    def getAllWarehouses(self, db: Session):
        return db.query(Warehouse).all()

    def createWarehouse(self, warehouse: WarehouseCreate, db: Session, current_user):
        user_id = current_user.id
        new_warehouse = Warehouse(
            warehouse_code=warehouse.warehouse_code,
            warehouse_name=warehouse.warehouse_name,
            location=warehouse.location,
            status=warehouse.status,
            warehouse_description=warehouse.warehouse_description,
            warehouse_type=warehouse.warehouse_type,
            warehouse_address=warehouse.warehouse_address,
            warehouse_stage=warehouse.warehouse_stage,
            quantity=warehouse.quantity,
            created_by = user_id
        )
        db.add(new_warehouse)
        db.commit()
        db.refresh(new_warehouse)
        return new_warehouse

    def getWarehouseById(self, warehouse_id: int, db: Session):
        warehouse_record = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
        if warehouse_record:
            return warehouse_record
        return None

    def updateWarehouse(self, warehouse_id: int, warehouse: WarehouseCreate, db: Session):
        warehouse_record = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
        if not warehouse_record:
            return None
        warehouse_record.warehouse_code = warehouse.warehouse_code
        warehouse_record.warehouse_name = warehouse.warehouse_name
        warehouse_record.location = warehouse.location
        warehouse_record.status = warehouse.status
        warehouse_record.warehouse_description = warehouse.warehouse_description
        warehouse_record.warehouse_type = warehouse.warehouse_type
        warehouse_record.warehouse_address = warehouse.warehouse_address
        warehouse_record.warehouse_stage = warehouse.warehouse_stage
        warehouse_record.quantity = warehouse.quantity
        db.commit()
        db.refresh(warehouse_record)
        return warehouse_record

    def deleteWarehouse(self, warehouse_id: int, db: Session):
        warehouse_record = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
        if not warehouse_record:
            return None
        db.delete(warehouse_record)
        db.commit()
        return warehouse_record

    def getAllTaxes(self, db: Session):
        return db.query(Tax).all()

    def createTax(self, tax: TaxCreate, db: Session, current_user):
        user_id = current_user.id
        new_tax = Tax(
            tax_code=tax.tax_code,
            tax_name=tax.tax_name,
            tax_rate=tax.tax_rate,
            status=tax.status,
            description=tax.description,
            created_by = user_id
        )
        db.add(new_tax)
        db.commit()
        db.refresh(new_tax)
        return new_tax

    def getTaxById(self, tax_id: int, db: Session):
        tax_record = db.query(Tax).filter(Tax.id == tax_id).first()
        if tax_record:
            return tax_record
        return None

    def updateTax(self, tax_id: int, tax: TaxCreate, db: Session):
        tax_record = db.query(Tax).filter(Tax.id == tax_id).first()
        if not tax_record:
            return None
        tax_record.tax_code = tax.tax_code
        tax_record.tax_name = tax.tax_name
        tax_record.tax_rate = tax.tax_rate
        tax_record.status = tax.status
        tax_record.description = tax.description
        db.commit()
        db.refresh(tax_record)
        return tax_record
    def createRequest(self, request: RequestHeaderCreate, db: Session, current_user):
        user_id = current_user.id
        new_request = RequestHeader(
            request_description = request.request_description,
            request_date = request.request_date,
            request_type = request.request_type,
            created_by = user_id
        )
        db.add(new_request)
        db.commit()
        db.refresh(new_request)

        for detail in request.details:
            new_detail = RequestDetail(
                header_id = new_request.id,
                product_id = detail.product_id,
                quantity = detail.quantity,
                unit_price = detail.unit_price,
                net_price = detail.net_price,
                more_detail = detail.more_detail,
                vat_id = detail.vat_id,
                vat_amount = detail.vat_amount
            )
            db.add(new_detail)

        db.commit()
        return new_request

    def getAllRequest(self, db: Session):
        headers = db.query(RequestHeader).all()
        details = db.query(RequestDetail).all()

        header_mapper = {header.id: [] for header in headers}
        for detail in details:
            if detail.header_id in header_mapper:
                header_mapper[detail.header_id].append(detail)

        request_results = []
        for header in headers:
            header_result = {
                "id": header.id,
                "request_description": header.request_description,
                "request_status": header.request_status,
                "request_type": header.request_type,
                "request_date": header.request_date,
                "details": header_mapper.get(header.id, [])
            }
            request_results.append(header_result)

        return request_results

    def getRequestPerId(self, request_id: int, db: Session):
        headers = db.query(RequestHeader).filter(RequestHeader.id == request_id).first()
        if not headers:
            None

        details = db.query(RequestDetail).filter(RequestDetail.header_id == request_id).all()
        results = {
            "id": headers.id,
            "request_description": headers.request_description,
            "request_status": headers.request_status,
            "request_type": headers.request_type,
            "request_date": headers.request_date,
            "details": details
        }
        return results

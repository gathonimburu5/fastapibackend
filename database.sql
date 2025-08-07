CREATE TABLE "public"."users" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "full_name" varchar(255),
  "email_address" varchar(255),
  "phone_number" varchar(20),
  "username" varchar(255),
  "password" varchar(255),
  "company_id" varchar(255),
  "status" varchar(100),
  "date_of_birth" date,
  "profile_picture" text,
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "users_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."products" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "product_code" varchar(255),
  "product_name" varchar(255),
  "product_type" varchar(20),
  "description" text,
  "buy_price" numeric(10, 2),
  "sell_price" numeric(10, 2),
  "quantity_per_unit" int4,
  "quantity" int4,
  "category_id" int4,
  "supplier_id" int4,
  "unit_id" int4,
  "reorder_level" int4,
  "product_image" text,
  "non_stock_item" varchar(50) DEFAULT 'no',
  "tax_id" int4,
  "warehouse_id" int4,
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "products_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."categories" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "category_name" varchar(255),
  "status" varchar(100) DEFAULT 'active',
  "description" text,
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "categories_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."measurement_units" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "unit_name" varchar(255),
  "status" varchar(100) DEFAULT 'active',
  "description" text,
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "measurement_units_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."warehouses" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "warehouse_code" varchar(255),
  "warehouse_name" varchar(255),
  "location" varchar(255),
  "status" varchar(100) DEFAULT 'active',
  "warehouse_description" text,
  "warehouse_type" varchar(100),
  "warehouse_address" varchar(100),
  "warehouse_stage" varchar(100),
  "quantity" int4 DEFAULT 0,
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "warehouses_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."taxes" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "tax_code" varchar(255),
  "tax_name" varchar(255),
  "tax_rate" numeric(5, 2),
  "status" varchar(100) DEFAULT 'active',
  "description" text,
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "taxes_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."employees" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "employee_name" varchar(255),
  "email_address" varchar(255),
  "id_number" varchar(20),
  "phone_number" varchar(20),
  "department" varchar(100),
  "postal_address" varchar(100),
  "date_of_birth" date,
  "date_of_joining" date,
  "physical_address" varchar(100),
  "designation" varchar(100),
  "salary" numeric(10, 2) DEFAULT 0.00,
  "status" varchar(100) DEFAULT 'active',
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "employees_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."customers" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "customer_name" varchar(255),
  "email_address" varchar(255),
  "phone_number" varchar(20),
  "postal_address" varchar(100),
  "physical_address" varchar(100),
  "date_of_birth" date,
  "date_of_registration" date,
  "vat_pin" varchar(20),
  "credit_limit" numeric(10, 2) DEFAULT 0.00,
  "sales_rep_id" int4,
  "status" varchar(100) DEFAULT 'active',
  "opening_balance" numeric(10, 2) DEFAULT 0.00,
  "opening_balance_date" date,
  "opening_balance_rate" numeric(10, 2) DEFAULT 0.00,
  "currency_id" int4,
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "customers_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."request_header" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "request_description" varchar(255),
  "request_date" date,
  "request_status" varchar(20) DEFAULT 'PENDING',
  "request_type" varchar(100),
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "request_header_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."request_detail" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "header_id" int4,
  "product_id" int4,
  "more_detail" varchar(255),
  "quantity" int4,
  "unit_price" numeric(10, 2) DEFAULT 0.00,
  "net_price" numeric(10, 2) DEFAULT 0.00,
  "vat_id" int4,
  "vat_amount" numeric(10, 2) DEFAULT 0.00,
  CONSTRAINT "request_detail_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."audit_trail" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "module_id" int4,
  "module_name" varchar(255),
  "action_taken" varchar(255),
  "user_id" int4,
  "created_on" date,
  CONSTRAINT "audit_trail_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."product_movement" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "product_id" int4,
  "open_stock" int4,
  "issued_qty" int4,
  "received_qty" int4,
  "adjusted_qty" int4,
  "physical_qty" int4,
  "transaction_name" varchar(255),
  "transaction_id" int4,
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "product_movement_pkey" PRIMARY KEY ("id")
);

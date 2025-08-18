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
  "business_certificate" text,
  "cr12_certificate" text,
  "business_permit" text,
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
  "business_certificate" text,
  "cr12_certificate" text,
  "business_permit" text,
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

CREATE TABLE "public"."warehouse_movement" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "product_id" int4,
  "warehouse_id" int4,
  "open_stock" int4,
  "issued_qty" int4,
  "received_qty" int4,
  "adjusted_qty" int4,
  "physical_qty" int4,
  "transfer_qty" int4,
  "transaction_name" varchar(255),
  "transaction_id" int4,
  "created_on" date,
  "created_by" int4,
  CONSTRAINT "warehouse_movement_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."sale_invoice_header" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "lpo_ref" int4,
  "invoice_amount" numeric(24,2),
  "delivery_address" varchar(255) COLLATE "pg_catalog"."default",
  "delivery_date" date,
  "invoice_date" date,
  "cust_id" int4,
  "due_date" date,
  "description" varchar(255) COLLATE "pg_catalog"."default",
  "created_on" date,
  "created_by" int4,
  "doc_prefix" varchar(255) COLLATE "pg_catalog"."default",
  "crn_reason" varchar(255) COLLATE "pg_catalog"."default",
  "has_credit_note" bool,
  "branch" int4,
  "invoice_balance" numeric(255,2),
  "credit_note_amount" numeric,
  "lpo_file" varchar(300) COLLATE "pg_catalog"."default",
  "entry_number" varchar(250) COLLATE "pg_catalog"."default",
  "rate" numeric(24,2) DEFAULT 1,
  "is_reversed" bool DEFAULT false,
  "statement_description" varchar(250) COLLATE "pg_catalog"."default",
  "invoice_number" int4,
  "crn_date" date,
  "crn_vat" numeric(20,2),
  "crn_vat_percent" varchar(24) COLLATE "pg_catalog"."default",
  PRIMARY KEY ("id")
);
CREATE TABLE "public"."sale_invoice_detail" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "header_id" int4,
  "vat_percent" text COLLATE "pg_catalog"."default",
  "vat_amt" numeric(24,2),
  "description" text COLLATE "pg_catalog"."default",
  "quantity" int4,
  "totals" numeric(24,2),
  "unit_price" numeric(24,5),
  "discount_perc" numeric(24,2),
  "discount_amt" numeric(24,2),
  "additional_details" varchar(255) COLLATE "pg_catalog"."default",
  "inventory_id" int4,
	PRIMARY KEY ("id")
);
CREATE TABLE "public"."sale_credit_note_detail" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "invoice_id" int4,
  "inventory_id" int4,
  "quantity" int4,
  "unit_price" numeric(24,2),
  "total_crn" numeric(24,2),
  "created_on" date,
  "created_by" int4,
  "description" varchar(255) COLLATE "pg_catalog"."default",
  "vat_per" int4,
  "vat_amount" numeric(24,2),
  PRIMARY KEY ("id")
);
CREATE TABLE "public"."sale_receipts" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "pay_date" date,
  "receipt_amount" numeric(100,2),
  "pay_mode" varchar(255) COLLATE "pg_catalog"."default",
  "cheque_number" varchar(255) COLLATE "pg_catalog"."default",
  "received_from" varchar(255) COLLATE "pg_catalog"."default",
  "additional_details" varchar(255) COLLATE "pg_catalog"."default",
  "created_on" date,
  "created_by" int4,
  "branch_id" int4,
  "status" varchar(50) COLLATE "pg_catalog"."default",
  "cust_id" int4,
  "rate" numeric(10,4),
  "allocation_remainder" numeric(100,2),
  "is_reversed" bool DEFAULT false,
	PRIMARY KEY ("id")
);
CREATE TABLE "public"."sale_receipts_details" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "inv_id" int4,
  "amount_allocated" numeric(100,2),
  "receipt_id" int4,
  "allocated_by" int4,
  "allocated_on" date,
  "description" varchar(1000) COLLATE "pg_catalog"."default",
  PRIMARY KEY ("id")
);
CREATE TABLE "public"."pl_invoice_header" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "supplier_id" int4,
  "lpo_ref" varchar(400) COLLATE "pg_catalog"."default",
  "invoice_date" date,
  "description" varchar(255) COLLATE "pg_catalog"."default",
  "created_by" int4,
  "created_on" date,
  "doc_prefix" varchar(255) COLLATE "pg_catalog"."default",
  "has_credit_note" bool,
  "due_date" date,
  "crn_date" date,
  "totals" numeric(30,2),
  "total_discount" numeric(30,2),
  "balance" numeric(30,2),
  "branch" int4,
  "entry_number" int4,
  "rate" numeric(10,4),
  "crn_total" numeric(30,0),
  "crn_vat" numeric(10,0),
  "crn_reference" varchar(100) COLLATE "pg_catalog"."default",
  "crn_vat_percent" varchar(24) COLLATE "pg_catalog"."default",
  "is_reversed" bool DEFAULT false,
	PRIMARY KEY ("id")
);
CREATE TABLE "public"."pl_invoice_detail" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
	"header_id" int4,
  "unit_price" numeric(19,2),
  "vat_percentage" varchar(24) COLLATE "pg_catalog"."default",
  "vat_amount" numeric(19,2),
  "description" varchar(100) COLLATE "pg_catalog"."default",
  "quantity" numeric(10,2),
  "discount_amt" numeric(19,2),
  "total" numeric(19,2),
  "inventory_id" int4,
	PRIMARY KEY ("id")
);
CREATE TABLE "public"."pl_receipts" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "pay_date" date,
  "paid_amount" numeric(10,2),
  "pay_mode" varchar(255) COLLATE "pg_catalog"."default",
  "cheque_number" varchar(255) COLLATE "pg_catalog"."default",
  "received_from" varchar(255) COLLATE "pg_catalog"."default",
  "payment_details" varchar(255) COLLATE "pg_catalog"."default",
  "created_on" date,
  "created_by" int4,
  "branch_id" int4,
  "rate" numeric(10,2),
  "supplier_id" int4,
  "allocation_remainder" numeric(10,2),
  "is_reversed" bool DEFAULT false,
  PRIMARY KEY ("id")
);
CREATE TABLE "public"."pl_receipts_details" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "inv_id" int4,
  "amount_allocated" numeric(100,2),
  "receipt_id" int4,
  "allocated_by" int4,
  "allocated_on" date,
  "description" varchar(1000) COLLATE "pg_catalog"."default",
  PRIMARY KEY ("id")
);
CREATE TABLE "public"."pl_credit_note_detail" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "invoice_id" int4,
  "inventory_id" int4,
  "quantity" int4,
  "unit_price" numeric(24,2),
  "total_crn" numeric(24,2),
  "created_on" date,
  "created_by" int4,
  "description" varchar(255) COLLATE "pg_catalog"."default",
  "vat_per" int4,
  "vat_amount" numeric(24,2),
  PRIMARY KEY ("id")
);
CREATE TABLE "public"."journal_header" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "journal_desc" varchar(200) COLLATE "pg_catalog"."default",
  "transaction_date" date,
  "trans_period" numeric(2,0),
  "tran_year" numeric(4,0),
  "tran_from" varchar(50) COLLATE "pg_catalog"."default",
  "sale_id" int8,
  "purchase_id" int8,
  "created_on" date,
	"created_by" int4,
  PRIMARY KEY ("id")
);
CREATE TABLE "public"."journal_details" (
    "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "journal_id" int4,
  "account_id" int4,
  "dr" numeric(10,2),
  "cr" numeric(10,2),
  "amount" numeric(10,2),
  "narration" varchar(255) COLLATE "pg_catalog"."default",
  "folio_no" varchar(100) COLLATE "pg_catalog"."default",
  PRIMARY KEY ("id")
);
CREATE TABLE "public"."accounts" (
	"id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "accounts_name" varchar(50) COLLATE "pg_catalog"."default",
  "group_id" int4,
  "opening_balance" numeric(10,2),
  "opening_balance_date" date,
  "has_opening_balance" bool DEFAULT false,
  "is_bank_acc" bool DEFAULT false,
	"created_on" date,
	"created_by" int4,
  PRIMARY KEY ("id")
);
CREATE TABLE "public"."account_groups" (
  "id" int4 NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1 MINVALUE  1 MAXVALUE 2147483647 START 1 CACHE 1),
  "group_name" varchar(50) COLLATE "pg_catalog"."default",
  "primary_group_code" varchar(6) COLLATE "pg_catalog"."default",
  "group_type" varchar(50) COLLATE "pg_catalog"."default",
  "group_sub_type" varchar(50) COLLATE "pg_catalog"."default",
  "group_level" int4,
	"created_on" date,
	"created_by" int4,
  PRIMARY KEY ("id")
);

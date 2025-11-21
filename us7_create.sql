-- Created by Redgate Data Modeler (https://datamodeler.redgate-platform.com)
-- Last modification date: 2025-11-20 20:37:21.723

DROP TABLE IF EXISTS Batch CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS Retail CASCADE;
DROP TABLE IF EXISTS Store CASCADE;
DROP TABLE IF EXISTS Shopper CASCADE;

-- tables
-- Table: Batch
CREATE TABLE Batch (
    batch_id int  NOT NULL,
    batch_status Batch_Status,
    shopper_id int  NOT NULL,
    CONSTRAINT Batch_pk PRIMARY KEY (batch_id)
);

-- Table: Order
CREATE TABLE orders (
    order_id int  NOT NULL,
    tips money  NOT NULL,
    order_fee money  NOT NULL,
    order_status Order_Status,
    store_id int  NOT NULL,
    batch_id int  NOT NULL,
    CONSTRAINT orders_pk PRIMARY KEY (order_id)
);

-- Table: Retail
CREATE TABLE Retail (
    retail_id int  NOT NULL,
    name text  NOT NULL,
    CONSTRAINT Retail_pk PRIMARY KEY (retail_id)
);

-- Table: Shopper
CREATE TABLE Shopper (
    shopper_id int  NOT NULL,
    shopping_status Shopping_Status,
    CONSTRAINT Shopper_pk PRIMARY KEY (shopper_id)
);

-- Table: Store
CREATE TABLE Store (
    store_id int  NOT NULL,
    location text  NOT NULL,
    retail_id int  NOT NULL,
    CONSTRAINT Store_pk PRIMARY KEY (store_id)
);

-- foreign keys
-- Reference: Batch_Shopper (table: Batch)
ALTER TABLE Batch ADD CONSTRAINT Batch_Shopper
    FOREIGN KEY (shopper_id)
    REFERENCES Shopper (shopper_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Batch (table: Order)
ALTER TABLE orders ADD CONSTRAINT Orders_Batch
    FOREIGN KEY (batch_id)
    REFERENCES Batch (batch_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Store (table: Order)
ALTER TABLE orders ADD CONSTRAINT Orders_Store
    FOREIGN KEY (store_id)
    REFERENCES Store (store_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Store_Retail (table: Store)
ALTER TABLE Store ADD CONSTRAINT Store_Retail
    FOREIGN KEY (retail_id)
    REFERENCES Retail (retail_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.


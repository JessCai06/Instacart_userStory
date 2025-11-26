-- Created by Redgate Data Modeler (https://datamodeler.redgate-platform.com)
-- Last modification date: 2025-11-26 22:41:55.458

DROP TABLE IF EXISTS Batch CASCADE;
DROP TABLE IF EXISTS Orders CASCADE;
DROP TABLE IF EXISTS Retail CASCADE;
DROP TABLE IF EXISTS Store CASCADE;
DROP TABLE IF EXISTS Shopper CASCADE;
DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Stock_Catalogue CASCADE;
DROP TABLE IF EXISTS Carted CASCADE;
DROP TABLE IF EXISTS Member CASCADE;
DROP TABLE IF EXISTS Nonmember CASCADE;
DROP TABLE IF EXISTS Payment CASCADE;
DROP TABLE IF EXISTS Promotion CASCADE;
DROP TABLE IF EXISTS Purchased CASCADE;


-- tables
-- Table: Batch
CREATE TABLE Batch (
    batch_id int  NOT NULL,
    batch_status Batch_Status  NOT NULL,
    shopper_id int  NOT NULL,
    CONSTRAINT Batch_pk PRIMARY KEY (batch_id)
);

-- Table: Carted
CREATE TABLE Carted (
    uid int  NOT NULL,
    bar_code int  NOT NULL,
    quantity int  NOT NULL,
    CONSTRAINT Carted_pk PRIMARY KEY (uid,bar_code)
);

-- Table: Member
CREATE TABLE Member (
    subscription_start timestamp  NOT NULL,
    subscription_duration interval  NOT NULL,
    autopay_on boolean  NOT NULL,
    has_paid boolean  NOT NULL,
    uid int  NOT NULL,
    CONSTRAINT Member_pk PRIMARY KEY (uid,subscription_start)
);

-- Table: Nonmember
CREATE TABLE Nonmember (
    uid int  NOT NULL,
    CONSTRAINT Nonmember_pk PRIMARY KEY (uid)
);

-- Table: Order
CREATE TABLE Orders (
    order_id int  NOT NULL,
    tips money  NOT NULL,
    order_fee money  NOT NULL,
    order_status Order_Status  NOT NULL,
    store_id int  NOT NULL,
    batch_id int  NOT NULL,
    uid int  NOT NULL,
    CONSTRAINT Order_pk PRIMARY KEY (order_id)
);

-- Table: Payment
CREATE TABLE Payment (
    pid int  NOT NULL,
    amount money  NOT NULL,
    date timestamp  NOT NULL,
    payment_method text  NOT NULL,
    paying_for Payment_Status  NOT NULL,
    uid int  NOT NULL,
    CONSTRAINT Payment_pk PRIMARY KEY (pid)
);

-- Table: Promotion
CREATE TABLE Promotion (
    promo_id text  NOT NULL,
    start_time timestamp  NOT NULL,
    end_time timestamp  NOT NULL,
    discount decimal  NOT NULL,
    CONSTRAINT Promotion_pk PRIMARY KEY (promo_id)
);

-- Table: Purchased
CREATE TABLE Purchased (
    bar_code int  NOT NULL,
    order_id int  NOT NULL,
    quantity int  NOT NULL,
    CONSTRAINT Purchased_pk PRIMARY KEY (order_id,bar_code)
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
    shopping_status Shopping_Status  NOT NULL,
    zipcode int  NOT NULL,
    CONSTRAINT Shopper_pk PRIMARY KEY (shopper_id)
);

-- Table: Store
CREATE TABLE Store (
    store_id int  NOT NULL,
    location text  NOT NULL,
    zipcode int  NOT NULL,
    retail_id int  NOT NULL,
    CONSTRAINT Store_pk PRIMARY KEY (store_id)
);

-- Table: User
CREATE TABLE Users (
    uid int  NOT NULL,
    name text  NOT NULL,
    phone int  NOT NULL,
    email text  NOT NULL,
    age int  NOT NULL,
    address text  NOT NULL,
    CONSTRAINT User_pk PRIMARY KEY (uid)
);

-- Table: stock_catalogue
CREATE TABLE Stock_Catalogue (
    bar_code int  NOT NULL,
    item_name text  NOT NULL,
    category text  NOT NULL,
    brand text  NOT NULL,
    stock_quantity int  NOT NULL,
    shelf_price money  NOT NULL,
    aisle int  NOT NULL,
    age_restricted boolean  NOT NULL,
    promo_id text  NOT NULL,
    CONSTRAINT stock_catalogue_pk PRIMARY KEY (bar_code)
);

-- foreign keys
-- Reference: Batch_Shopper (table: Batch)
ALTER TABLE Batch ADD CONSTRAINT Batch_Shopper
    FOREIGN KEY (shopper_id)
    REFERENCES Shopper (shopper_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Carted_User (table: Carted)
ALTER TABLE Carted ADD CONSTRAINT Carted_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Member_User (table: Member)
ALTER TABLE Member ADD CONSTRAINT Member_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Nonmember_User (table: Nonmember)
ALTER TABLE Nonmember ADD CONSTRAINT Nonmember_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Batch (table: Order)
ALTER TABLE Orders ADD CONSTRAINT Orders_Batch
    FOREIGN KEY (batch_id)
    REFERENCES Batch (batch_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Purchased (table: Purchased)
ALTER TABLE Purchased ADD CONSTRAINT Orders_Purchased
    FOREIGN KEY (order_id)
    REFERENCES Orders (order_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Store (table: Order)
ALTER TABLE Orders ADD CONSTRAINT Orders_Store
    FOREIGN KEY (store_id)
    REFERENCES Store (store_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_User (table: Order)
ALTER TABLE Orders ADD CONSTRAINT Orders_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Payment_User (table: Payment)
ALTER TABLE Payment ADD CONSTRAINT Payment_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Purchased_stock_catalogue (table: Purchased)
ALTER TABLE Purchased ADD CONSTRAINT Purchased_Stock_Catalogue
    FOREIGN KEY (bar_code)
    REFERENCES Stock_Catalogue (bar_code)  
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

-- Reference: stock_catalogue_Carted (table: Carted)
ALTER TABLE Carted ADD CONSTRAINT Stock_Catalogue_Carted
    FOREIGN KEY (bar_code)
    REFERENCES Stock_Catalogue (bar_code)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: stock_catalogue_Promotion (table: stock_catalogue)
ALTER TABLE Stock_Catalogue ADD CONSTRAINT Stock_Catalogue_Promotion
    FOREIGN KEY (promo_id)
    REFERENCES Promotion (promo_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.


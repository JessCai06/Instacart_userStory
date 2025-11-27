-- drop the trax database if it exists
DROP database if EXISTS instacart;

SET datestyle = 'ISO, MDY';

-- create it afresh
CREATE database instacart;
\c instacart


DROP TYPE IF EXISTS Order_Status CASCADE;
DROP TYPE IF EXISTS Batch_Status CASCADE;
DROP TYPE IF EXISTS Shopping_Status CASCADE;
DROP TYPE IF EXISTS Payment_Status CASCADE;

CREATE TYPE Order_Status AS ENUM('Issued', 'Assigned', 'Picked_up', 'Shopping', 'Delivered', 'Cancelled');
CREATE TYPE Batch_Status AS ENUM ('Unassigned','Assigned', 'In_progress', 'Completed', 'Cancelled');
CREATE TYPE Shopping_Status AS ENUM('Available', 'Shopping', 'On_break');
CREATE TYPE Payment_Status as ENUM('Order', 'Membership');


\i final_create.sql


\copy Retail(retail_id, name) FROM data/retail.csv csv header;
\copy Shopper(shopper_id, shopping_status,zipcode) FROM data/shopper.csv csv header;
\copy Store(store_id, location, retail_id,zipcode) FROM data/store.csv csv header;
\copy Batch(batch_id, batch_status, shopper_id) FROM data/batch.csv csv header;
\copy Users(uid, name, phone, email, age, address) FROM data/user.csv csv header;
\copy Orders(order_id, tips, order_fee, order_status, store_id, batch_id, uid) FROM data/order.csv csv header;
\copy Member(uid, subscription_start, subscription_duration, autopay_on, has_paid) FROM data/member.csv csv header;
\copy Nonmember(uid) FROM data/nonmember.csv csv header;
\copy Payment(pid, amount, date, payment_method, paying_for, uid) FROM data/payment.csv csv header;
\copy Stock_Catalogue(bar_code,item_name,category,brand,stock_quantity,shelf_price,aisle,age_restricted,store_id,promo_id) FROM data/stock_catalogue.csv csv header;
\copy Carted(uid, bar_code, quantity) FROM data/user_cart.csv csv header;
\copy Purchased(bar_code, order_id, quantity) FROM data/user_purchased.csv csv header;


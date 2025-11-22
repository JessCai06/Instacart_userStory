-- drop the trax database if it exists
DROP database if EXISTS instacart;

SET datestyle = 'ISO, MDY';

-- create it afresh
CREATE database instacart;
\c instacart


DROP TYPE IF EXISTS Order_Status CASCADE;
DROP TYPE IF EXISTS Batch_Status CASCADE;
DROP TYPE IF EXISTS Shopping_Status CASCADE;

CREATE TYPE Order_Status AS ENUM('issued', 'assigned', 'picked_up', 'shopping', 'delivered', 'cancelled');
CREATE TYPE Batch_Status AS ENUM ('Unassigned','Assigned', 'In_progress', 'Completed', 'Cancelled');
CREATE TYPE Shopping_Status AS ENUM('Available', 'Shopping', 'On_break');

\i us7_create.sql



\copy Retail(retail_id, name) FROM data/retail.csv csv header;
\copy Shopper(shopper_id, shopping_status) FROM data/shopper.csv csv header;
\copy Store(store_id, location, retail_id) FROM data/store.csv csv header;
\copy Batch(batch_id, batch_status, shopper_id) FROM data/batch.csv csv header;
\copy Orders(order_id, tips, order_fee, order_status, store_id, batch_id) FROM data/order.csv csv header;


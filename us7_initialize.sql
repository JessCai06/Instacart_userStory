-- drop the trax database if it exists
DROP database if EXISTS instacart;

SET datestyle = 'ISO, MDY';

-- create it afresh
CREATE database instacart;
\c instacart


DROP IF EXISTS Order_Status
DROP IF EXISTS Batch_Status
DROP IF EXISTS Shopping_Status

CREATE TYPE Order_Status AS ENUM('Issued', 'Assigned', 'Picked_up', 'Delivered');
CREATE TYPE Batch_Status AS ENUM ('Unassigned','Assigned', 'In_progress', 'Completed', 'Cancelled');
-- better to revise shopping status to "shopper availability" status
CREATE TYPE Shopping_Status AS ENUM('Available', 'Shopping', 'On_break');


-- load the data

\copy Batch(batch_id, batch_status, shopper_id) FROM batch.csv csv header;
\copy Order(order_id, tips, order_fee, order_status, store_id, batch_id) FROM order.csv csv header;
\copy Shopper(shopper_id, shopping_status) FROM shopper.csv csv header;
\copy Store(store_id, location, retail_id) FROM store.csv csv header;
\copy Retail(retail_id, name) FROM retail.csv csv header;


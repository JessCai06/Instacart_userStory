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

\copy Users(uid, name, role) FROM data/users.csv csv header;
\copy Issues(iid, initial_date, product, status, priority, uid, message) FROM data/issues.csv csv header;
\copy Bugs(bid, severity) FROM data/bugs.csv csv header;
\copy Features(fid, votes) FROM data/features.csv csv header;
\copy Comments(cid, date, iid, uid, comment) FROM data/comments.csv csv header;


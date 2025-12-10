-- Connect to your project database (grader runs from postgres)
\c project

\echo
\echo 'show all below ---------------'

\echo 'Retail  - one row per retail chain (e.g., Costco, Target, Whole Foods)'
SELECT * FROM retail;
\echo

\echo 'Store   - individual physical store locations belonging to a retail chain'
SELECT * FROM store;
\echo

\echo 'Shopper - shoppers who pick and deliver orders'
SELECT * FROM shopper;
\echo

\echo 'Batch   - groups of orders assigned to a shopper'
SELECT * FROM batch;
\echo

\echo 'Orders  - individual customer orders linked to a store and a batch'
SELECT * FROM orders;
\echo

\echo 'Users   - individual users who place orders'
SELECT * FROM users;
\echo

\echo 'Member  - users who have a membership subscription'
SELECT * FROM member;
\echo

\echo 'Nonmember - users who do not have a membership subscription'
SELECT * FROM nonmember;
\echo

\echo 'Payment - payments made by users for orders or memberships'
SELECT * FROM payment;
\echo

\echo 'Promotion - promotional discounts available on certain items'
SELECT * FROM promotion;
\echo

\echo 'Stock_Catalogue - items available in stores, including pricing and promotions'
SELECT * FROM stock_catalogue;
\echo

\echo 'Carted - items that users have added to their shopping carts'
SELECT * FROM carted;
\echo

\echo 'Purchased - items that users have purchased in their orders'
SELECT * FROM purchased;
\echo

\echo '------------------------------'
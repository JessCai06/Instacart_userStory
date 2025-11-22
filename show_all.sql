-- Connect to your project database (grader runs from postgres)
\c instacart

\echo
\echo 'show all below ---------------'

\echo 'Retail  — one row per retail chain (e.g., Costco, Target, Whole Foods)'
SELECT * FROM retail;
\echo

\echo 'Store   — individual physical store locations belonging to a retail chain'
SELECT * FROM store;
\echo

\echo 'Shopper — shoppers who pick and deliver orders'
SELECT * FROM shopper;
\echo

\echo 'Batch   — groups of orders assigned to a shopper'
SELECT * FROM batch;
\echo

\echo 'Orders  — individual customer orders linked to a store and a batch'
SELECT * FROM orders;
\echo


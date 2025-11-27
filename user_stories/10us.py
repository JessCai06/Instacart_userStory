from common import *

us = '''
* Simple US07: Update Order Delivery Status

   As a user, I want to see the location of the shoppers who are actively delivering and making deliveries close to the store I want to shop at, so that I know delivery coverage in that area and can plan accordingly.


'''

print(us)

def update_delivery_status(retail):
    tmpl = b'''
DROP FUNCTION IF EXISTS fn_update_order_status() CASCADE;

CREATE FUNCTION fn_get_shoppers_location()
RETURNS table(store text, zipcode integer, active_shoppers integer)
LANGUAGE plpgsql AS
$$
BEGIN
    SELECT s.name, s.zipcode, COUNT(h.shopper_id) as active_shoppers
      FROM Store as s
           JOIN Retail as r ON (r.retail_id = s.retail_id)
           JOIN Orders as o ON (s.store_id = o.store_id)
           JOIN Batch as b ON (o.batch_id = b.batch_id)
           JOIN Shopper as h ON (b.shopper_id = h.shopper_id)
     WHERE (h.zipcode = s.zipcode)
           AND (h.shopper_status = 'Available')
           AND (s.retail_id = %s)
     GROUP BY s.name, s.zipcode
END;
$$;

DROP TRIGGER IF EXISTS tr_update_order_status ON batch;

CREATE TRIGGER tr_update_order_status
AFTER UPDATE OF batch_status ON batch
FOR EACH ROW
EXECUTE FUNCTION fn_update_order_status();
'''
    cmd = tmpl
    print_cmd(cmd)
    cur.execute(cmd)


# resetting data

reset = """
    UPDATE batch
       SET batch_status = 'In_progress'
     WHERE batch_id = 301;
    
    UPDATE Orders
       SET order_status = 'Issued'
     WHERE order_id = 401;

    UPDATE Orders
       SET order_status = 'Shopping'
     WHERE order_id = 402;
"""

cur.execute(reset)
cur.connection.commit()

# testing our trigger
update_delivery_status_trigger()

cols_str = 'order_id tips order_fee order_status store_id batch_id'
cols_strr = 'batch_id batch_status shopper_id'


print("\n\nBATCH BEFORE")
cur.execute("SELECT * FROM Batch ORDER BY batch_id;")
rows_before = cur.fetchall()
show_table(rows_before, cols_strr)

print("\n\nORDERS BEFORE")
cur.execute("SELECT * FROM Orders ORDER BY order_id;")
rows_before = cur.fetchall()
show_table(rows_before, cols_str)


trigcommand = """
    UPDATE batch
        SET batch_status = 'Completed'
      WHERE batch_id = 301;
"""


print("\n\nTrigger: updating batch_id 301 from 'In_prorgress' to 'Completed'")
# print(trigcommand)
cur.execute(trigcommand)
cur.connection.commit()

print("\n\nBATCH AFTER")
cur.execute("SELECT * FROM Batch ORDER BY batch_id;")
rows_after = cur.fetchall()
show_table(rows_after, cols_strr)

print("\n\nORDERS AFTER")
cur.execute("SELECT * FROM Orders ORDER BY order_id;")
rows_after = cur.fetchall()
show_table(rows_after, cols_str)



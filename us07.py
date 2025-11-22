from common import *

us = '''
* Simple US07: Update Order Delivery Status

   As a Shopper, I want to be able to update the delivery status of my assigned orders with the batch status, so that customers can track real-time 
   progress of their grocery delivery.
'''

print(us)

def update_delivery_status_trigger():
    tmpl = b'''
DROP FUNCTION IF EXISTS fn_update_order_status() CASCADE;

CREATE FUNCTION fn_update_order_status()
RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
BEGIN
    -- When batch becomes completed, mark related orders as Delivered
    IF OLD.batch_status <> 'Completed' AND NEW.batch_status = 'Completed' THEN
        UPDATE Orders
           SET order_status = 'Delivered'
         WHERE batch_id = NEW.batch_id;
    END IF;

    RETURN NEW;
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

print("\n\nBEFORE (Orders)")
cur.execute("SELECT * FROM Orders ORDER BY order_id;")
rows_before = cur.fetchall()
show_table(rows_before, cols_str)

print("\n\nBEFORE (Batch)")
cur.execute("SELECT * FROM Batch ORDER BY batch_id;")
rows_before = cur.fetchall()
show_table(rows_before, cols_strr)

trigcommand = """
    UPDATE batch
        SET batch_status = 'Completed'
      WHERE batch_id = 301;
"""
print("trigger we're updating batch to completed")
# print(trigcommand)
cur.execute(trigcommand)
cur.connection.commit()

print("\n\nAFTER (Orders)")
cur.execute("SELECT * FROM Orders ORDER BY order_id;")
rows_after = cur.fetchall()
show_table(rows_after, cols_str)

print("\n\nAFTER (Batch)")
cur.execute("SELECT * FROM Batch ORDER BY batch_id;")
rows_after = cur.fetchall()
show_table(rows_after, cols_strr)


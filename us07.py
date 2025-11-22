from common import *

us='''
* Simple US07: Update Order Delivery Status

   As a Shopper, I want to be able to update the delivery status of my assigned orders (e.g., “picked up,” “in transit,” “delivered”), so that customers can track real-time progress of their grocery deliver. 
'''

print(us)

def update_delivery_status():
    
    tmpl = f'''

DROP FUNCTION IF EXISTS fn_update_order_status () CASCADE;    
CREATE FUNCTION fn_update_order_status ()
RETURNS trigger
LANGUAGE plpgsql AS
$$
BEGIN
  IF (old.batch_status != 'Completed' AND new.batch_status = 'Completed') THEN
    UPDATE Orders
       SET order_status = 'delivered'
     WHERE Batch.batch_id = new.batch_id;
  END IF;
RETURN null;
END;
$$;

DROP TRIGGER IF EXISTS tr_update_order_status ON Batch;

CREATE TRIGGER tr_update_order_status
AFTER UPDATE OF batch_status ON Batch
FOR EACH ROW
EXECUTE FUNCTION fn_update_order_status ();
'''
    


    cmd = cur.mogrify(tmpl, ())
    print_cmd(cmd)
    cur.execute(cmd)
    cur.connection.commit()
    # rows = cur.fetchall()
    # pp(rows)
    # show_table( rows, cols )

update_delivery_status()    

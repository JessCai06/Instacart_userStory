from common import *

us='''
* Simple US07: Update Order Delivery Status

   As a:  Shopper
 I want:  I want to be able to update the delivery status of my assigned orders (e.g., “picked up,” “in transit,” “delivered”)
So that customers can track real-time progress of their grocery deliver
simple
So That:  operational
'''

print(us)

def update_delivery_status():
    
    tmpl = f'''
CREATE FUNCTION fn_update_order_status ()
RETURNS trigger
LANGUAGE plpgsql AS
$$
BEGIN
  IF (old.batch_status != 'Delivered' AND new.batch_status = 'Delivered') THEN
    UPDATE "order"
       SET order_status = 'Delivered'
     WHERE batch_id = new.batch_id;
  END IF;
RETURN null;
END;
$$;


CREATE TRIGGER tr_update_order_status
AFTER UPDATE OF batch_status ON "batch"
FOR EACH ROW
EXECUTE FUNCTION fn_update_order_status ();
'''
    


    cmd = cur.mogrify(tmpl, ())
    print_cmd(cmd)
    cur.execute(cmd)
    # rows = cur.fetchall()
    # pp(rows)
    # show_table( rows, cols )

update_delivery_status()    

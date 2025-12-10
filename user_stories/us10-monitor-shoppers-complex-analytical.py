from common import *

us = '''
* Simple US07: Update Order Delivery Status

   As a user, I want to see the location of the shoppers who are actively delivering and making deliveries close to the store I want to shop at, so that I know delivery coverage in that area and can plan accordingly.


'''

print(us)

def update_delivery_status(retail):
    tmpl = b'''
DROP FUNCTION IF EXISTS fn_get_shoppers_location(int) CASCADE;

CREATE FUNCTION fn_get_shoppers_location(p_retail_id int)
RETURNS table(store text, zipcode int, active_shoppers bigint)
LANGUAGE plpgsql AS
$$
BEGIN
    RETURN QUERY

    SELECT r.name, s.zipcode, COUNT(DISTINCT h.shopper_id) as active_shoppers
      FROM Store as s
           JOIN Retail as r ON (r.retail_id = s.retail_id)
           JOIN Orders as o ON (s.store_id = o.store_id)
           JOIN Batch as b ON (o.batch_id = b.batch_id)
           LEFT JOIN Shopper as h ON (b.shopper_id = h.shopper_id)
     WHERE (h.zipcode = s.zipcode)
           AND (h.shopping_status = 'Available')
           AND (s.retail_id = p_retail_id)
     GROUP BY r.name, s.zipcode;
END;
$$;

'''
    cmd = tmpl
    print_cmd(cmd)
    cur.execute(cmd)

    cur.execute("SELECT * FROM fn_get_shoppers_location(%s);", (retail,))
    rows = cur.fetchall()
    cols = 'r.name s.zipcode active_shoppers'
    print("rows =", rows)
    show_table(rows, cols)


update_delivery_status(1)
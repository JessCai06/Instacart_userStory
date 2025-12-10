from common import *

us = '''
* Simple Operational US05: Track progress

   As a user, I want to track the progress of my shopper so that I can monitor the status of my order.
'''

print(us)

def track_shopper_progress(order_id):
    tmpl =  '''
   SELECT h.shopping_status
     FROM Orders as o
          JOIN Batch as b ON (o.batch_id = b.batch_id)
          JOIN Shopper as h ON (b.shopper_id = h.shopper_id)
    WHERE o.order_id = %s
    
'''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(tmpl, (order_id,))
    rows = cur.fetchall()
    show_table(rows)

track_shopper_progress(401)
track_shopper_progress(403)


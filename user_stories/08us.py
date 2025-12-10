from common import *

us = '''
* Simple Operational US08: See popular items

   As an Instacart manager, I want to be able to see the items that customers purchase for the most, so that I would know what items I should display on the front page.


'''

print(us)

def list_popular_items(limit):
    tmpl =  '''

    SELECT c.bar_code, c.item_name, SUM(p.quantity) as times_purchased
      FROM Stock_Catalogue as c
           JOIN Purchased as p ON (c.bar_code = p.bar_code)
     GROUP BY c.bar_code, c.item_name
     ORDER BY times_purchased DESC
     LIMIT %s;
    
'''
    cmd = cur.mogrify(tmpl)
    params = (limit,)
    print_cmd(cmd)
    cur.execute(tmpl, params)
    rows = cur.fetchall()
    show_table(rows)

list_popular_items(2)

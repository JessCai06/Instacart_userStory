from common import *

us = '''
* Simple Analytical US01: Order results

   As a user, I want to be able to order my search results by price from low to high across different grocery stores, so that I can choose the best store option and spend less.
'''

print(us)

def list_price_desc(search_term):
    tmpl =  '''
   select item_name, shelf_price, store_id
        from stock_catalogue
    where item_name ILIKE %s
    order by shelf_price ASC;
    
'''
    param = ('%' + search_term + '%',)
    cmd = cur.mogrify(tmpl, param)
    print_cmd(cmd)
    cur.execute(tmpl, param)
    rows = cur.fetchall()
    show_table(rows)

list_price_desc("Apple")    
list_price_desc("milk")    


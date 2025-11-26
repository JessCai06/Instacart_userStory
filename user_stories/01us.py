from common import *

us = '''
* Simple US01: Order results

   As a user, I want to be able to order my search results by price from low to high across different grocery stores
So that I can choose the best store option and spend less
'''

print(us)

def list_price_desc(search_term):
    tmpl =  f'''
   select item_name, price, store_id
        from stock_catalogue
    where item_name ILIKE %s
    order by price DESC;
    
'''
    cmd = cur.mogrify(tmpl, ())
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows)

list_price_desc("apple")    
list_price_desc("milk")    


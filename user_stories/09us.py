from common import *

us = '''
* Complex Analytical US09: See average time
    As an instacart Manager, I want to see the average time that it took for 
    shoppers to fulfill assigned batches of 1, 2 or 3 orders so that I would 
    know when it is better for Instacart to have one shopper shop for multiple 
    orders, and when it is better to have multiple shoppers only shop for one order
'''

print(us)

def list_price_desc(search_term):
    tmpl =  '''
   
    
'''
    param = ('%' + search_term + '%',)
    cmd = cur.mogrify(tmpl, param)
    print_cmd(cmd)
    cur.execute(tmpl, param)
    rows = cur.fetchall()
    show_table(rows)

list_price_desc("Apple")    
list_price_desc("milk")    


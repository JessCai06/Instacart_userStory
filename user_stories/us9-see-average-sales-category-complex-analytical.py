from common import *

us = '''
* Complex Analytical US09: See average sales by category
    As a grocery store staff, I want to see which category is the most purchased, so that I would know what to prioritize when I display items on the store website.
'''

print(us)

def sales_by_category():
    tmpl =  '''
        SELECT DISTINCT c.category, AVG(p.quantity) over wd as avg
          FROM Purchased as p
               JOIN stock_catalogue as c ON (p.bar_code = c.bar_code)
        WINDOW wd as (PARTITION BY c.category)
         ORDER BY avg DESC
    
'''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(tmpl)
    rows = cur.fetchall()
    cols = 'c.category avg'
    show_table(rows, cols)

sales_by_category()

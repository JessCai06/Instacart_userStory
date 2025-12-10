from common import *

us = '''
* Complex Analytical US09: See average sales by category
    As a grocery store staff, I want to see which category is the most purchased,
    so that I would know what to prioritize when I display items on the store website.
'''

print(us)

def sales_by_category():
    tmpl = '''
        SELECT DISTINCT
               c.category,
               ROUND(AVG(p.quantity) OVER wd, 2) AS avg
        FROM purchased AS p
        JOIN stock_catalogue AS c
          ON p.bar_code = c.bar_code
        WINDOW wd AS (PARTITION BY c.category)
        ORDER BY avg DESC;
    '''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(tmpl)
    rows = cur.fetchall()
    cols = 'category avg'
    show_table(rows, cols)

sales_by_category()

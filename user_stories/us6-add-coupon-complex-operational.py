from common import *

us = '''
* Simple Operational US06: Track progress

   As a grocery store staff, I want to be able to add a coupon to an item, which will reduce that item's price, so that they can attract customers with discounts.


'''

print(us)

def add_coupon(bar_code, promo):
    tmpl =  '''

    UPDATE stock_catalogue
       SET promo_id = %s
     WHERE bar_code = %s;

    UPDATE stock_catalogue
       SET shelf_price = shelf_price * (1 - ( SELECT discount
                                                 FROM Promotion
                                                WHERE promo_id = %s
                                            ))
    WHERE bar_code = %s;
    
'''
    cmd = cur.mogrify(tmpl)
    params = (promo, bar_code, promo, bar_code)
    print_cmd(cmd)
    cur.execute(tmpl, params)



# testing the update

cols_strr = 'bar_code item_name category brand stock_quantity shelf_price aisle age_restricted store_id promo_id'

print('------------------------TEST CASE 1----------------------------')
add_coupon(1002, "PROMO0")

print("\n\nstock_catalogue BEFORE")
cur.execute("SELECT * FROM stock_catalogue")
rows_before = cur.fetchall()
show_table(rows_before, cols_strr)

print('------------------------TEST CASE 2----------------------------')
add_coupon(1002, "PROMO1")

print("\n\nstock_catalogue AFTER")
cur.execute("SELECT * FROM stock_catalogue")
rows_after = cur.fetchall()
show_table(rows_after, cols_strr)

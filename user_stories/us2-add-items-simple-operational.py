from common import *

us = '''
* Simple Operational US02: Add Items to Shopping Cart

   As a user, I want to be able to add items to my shopping cart and specify the quantity
So that I can purchase all of them together when I check out
'''

print(us)

def update_cart(barcode, quantity, uid):
    fn_sql = '''
    CREATE OR REPLACE FUNCTION fn_update_cart(
        p_bar_code INT,
        p_quantity INT,
        p_uid INT
    )
    RETURNS void
    LANGUAGE plpgsql
    AS $$
    BEGIN
        -- If this barcode is already in the cart for this user, bump the quantity
        IF EXISTS (
            SELECT 1
            FROM carted
            WHERE bar_code = p_bar_code
              AND uid = p_uid
        ) THEN
            UPDATE carted
            SET quantity = quantity + p_quantity
            WHERE bar_code = p_bar_code
              AND uid = p_uid;
        ELSE
            INSERT INTO carted (bar_code, quantity, uid)
            VALUES (p_bar_code, p_quantity, p_uid);
        END IF;
    END;
    $$;
    '''

    cur.execute(fn_sql)

    print("Shopping Cart before adding items:")
    show_this_table('carted')

    print('We are putting item %s with quantity %s into user %s \'s cart' % (barcode, quantity, uid))

    print("Shopping Cart after adding items:")
    show_this_table('carted')
    print("\n")


# Test the function
print('------------------------TEST CASE 1----------------------------')
update_cart(1001, 3, 2)
print('------------------------TEST CASE 2----------------------------')
update_cart(1003, 4, 5)

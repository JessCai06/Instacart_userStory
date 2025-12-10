from common import * 

us = '''
* Complex Analytical US04: Compare inventory

  As a Grocery Store Staff member,
  I want to see, for a given store, each item’s current stock alongside the total quantity
  in all orders,
  So that I can identify items that are at risk of going out of stock before shoppers arrive
  and restock them in advance.
'''

print(us)


def compare_inventory(store_id):
    sql = b'''
        WITH incoming AS (
            SELECT
                sc.bar_code,
                COALESCE(SUM(p.quantity), 0) AS incoming_quantity
            FROM stock_catalogue AS sc
            LEFT JOIN purchased AS p
              ON sc.bar_code = p.bar_code
            GROUP BY sc.bar_code
        ),
        inventory AS (
            SELECT
                sc.bar_code,
                sc.item_name,
                sc.stock_quantity,
                COALESCE(i.incoming_quantity, 0) AS incoming_quantity,
                sc.stock_quantity - COALESCE(i.incoming_quantity, 0) AS remaining_after_orders
            FROM stock_catalogue sc
            LEFT JOIN incoming i
              ON sc.bar_code = i.bar_code
            LEFT JOIN store s
              ON sc.store_id = s.store_id
            WHERE sc.store_id = %s
        )
        SELECT
            bar_code,
            item_name,
            stock_quantity,
            incoming_quantity,
            remaining_after_orders,
            CASE
                WHEN remaining_after_orders < 0 THEN 'RESTOCK_IMMEDIATELY'
                WHEN remaining_after_orders BETWEEN 0 AND 9 THEN 'CRITICAL_LOW'
                WHEN remaining_after_orders BETWEEN 10 AND 29 THEN 'LOW'
                ELSE 'SUFFICIENT'
            END AS stock_flag
        FROM inventory
        ORDER BY
            item_name;
    '''

    print_cmd(sql)
    cur.execute(sql, (store_id,))
    rows = cur.fetchall()

    print(f"\n=== Stock vs incoming orders for store {store_id} ===")
    show_table(
        rows,
        cols='bar_code item_name stock_quantity incoming_quantity remaining_after_orders stock_flag'
    )


# remember: store_ids are 101–104
compare_inventory(101)

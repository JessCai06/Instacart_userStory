from common import *

us = '''
* Simple Analytical US03: See Orders

  As a shopper, I want to be able to see order details such as the grocery store, the distance the customer is from the store, and the delivery time 
So that I can plan accordingly and bulk several deliveries for one shopping run
'''

print(us)


_distance_lookup = {
    (1, 101): 9,   # Katie Smith to shadyside
    (2, 101): 2,   # Alex Lee to shadyside
    (2, 102): 9,   # Alex Lee to east Liberty
    (1, 103): 5,   # Katie Smith to Pittsburgh - Waterfront
    (3, 103): 4,   # Maria Gomez to oakland
    (3, 102): 8,   # Maria Gomez to east Liberty
    (4, 102): 2,   # Sam Patel to east Liberty
}

def compute_distance(uid, store_id):
    """
    Return the (fake) distance in miles between the user and the store

    In production, this function would:
      - Look up the user address and store address in the database
      - Geocode them to latitude/longitude
      - Call a routing/distance API to get driving distance

    For this project, we will look up a pre-defined value from the _distance_lookup so that our test cases are stable.
    """
    return _distance_lookup.get((uid, store_id), 0)


def estimate_delivery_minutes(distance_miles):
    """
    Very rough heuristic: 10 minutes per mile + 5 minutes buffer.
    In a real system, this would use live traffic + batching logic.
    """
    return distance_miles * 10 + 5


def see_order_details():
    fn_sql = b'''
        SELECT
            o.order_id,
            u.uid,
            u.name       AS customer_name,
            s.store_id,
            s.location   AS store_location,
            o.order_status,
            o.tips,
            o.order_fee
        FROM Orders AS o
        JOIN Users  AS u USING (uid)
        JOIN Store  AS s USING (store_id)
        WHERE o.order_status = 'Issued'
        ORDER BY o.order_id;
    '''

    print_cmd(fn_sql)
    cur.execute(fn_sql)
    rows = cur.fetchall()

    enriched_rows = []
    for (order_id,
         uid,
         customer_name,
         store_id,
         store_location,
         order_status,
         tips,
         order_fee) in rows:

        dist = compute_distance(uid, store_id)
        eta  = estimate_delivery_minutes(dist)

        enriched_rows.append((
            order_id,
            customer_name,
            store_location,
            dist,         
            eta,           
            order_status,
            tips,
            order_fee
        ))

    show_table(
        enriched_rows,
        cols='order_id customer_name store_location distance_miles est_delivery_min order_status tips order_fee'
    )


see_order_details()

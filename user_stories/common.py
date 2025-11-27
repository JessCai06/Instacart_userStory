import psycopg2
from pprint import pprint as pp
from prettytable import PrettyTable

import re

def show_this_table(table_name):
    cmd = b'''
        SELECT * FROM ''' + table_name.encode('utf-8') + b''';
    '''
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows,get_cols_str(table_name))

def c(s):
    return re.sub('\s+', ', ', s)

def get_cols_str(table_name: str) -> str:

    sql = """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = %s
        ORDER BY ordinal_position;
    """
    cur.execute(sql, (table_name,))
    cols = [row[0] for row in cur.fetchall()]
    return " ".join(cols)

def show_table(rows, cols='', ncols=None):
    if ncols != None:
        cols = [('c%d' % i) for i in range(1, ncols+1)]
    else:
        cols = cols.split()
    table = PrettyTable( cols )
    table.add_rows(rows)
    print(table)


SHOW_CMD = True

def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

conn = psycopg2.connect(database='instacart', user='isdb')
conn.autocommit = True
cur = conn.cursor()



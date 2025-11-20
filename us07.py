from common import *

us='''
* Simple US

   As a:  Manager
 I want:  To see all the unresolved bugs
So That:  I can see what needs to be addressed
'''

print(us)

def list_unresolved_bugs():

    cols = 'b.bid b.severity i.initial_date i.product i.status i.priority u.uid u.name u.role'

    tmpl =  f'''
SELECT {c(cols)}
  FROM Bugs as b
       JOIN Issues as i ON b.bid = i.iid
       JOIN Users as u ON i.uid = u.uid
 WHERE i.status <> 'resolved'
 ORDER BY b.severity DESC    
'''
    cmd = cur.mogrify(tmpl, ())
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    # pp(rows)
    show_table( rows, cols )

list_unresolved_bugs()    

import sqlite3
import audio
con= sqlite3.connect('stugentgu.db')
cur=con.cursor()
cur.execute("select * from stud")
x=cur.fetchall()
con.close()
print("detail is")
for stud in x:
    print("name",stud[0])
    print("salary",stud[1],"\n")
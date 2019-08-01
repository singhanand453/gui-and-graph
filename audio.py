import sqlite3
#name=input("enter your name")
#salary=int(input("enter your salary"))
con=sqlite3.connect('stugentgu.db')
cur=con.cursor()
#cur.execute("create table stud(name text,salary integer ) ")
#cur.execute("insert into stud(name,salary) values(?,?)",(name,salary))
#cur.execute("update stud set salary=5000 where name='naman'")
cur.execute("")
cur.execute("Select * from stud")
print(cur.fetchall())
con.commit()
con.close();
#print("data saved successfully")



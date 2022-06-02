import mysql.connector;
conn=mysql.connector.connect(host='localhost',database='akash',user='root',password='0707')
if conn.is_connected():
    print("connected to database successfully")
cursor=conn.cursor()
cursor.execute("insert into stud_tab values(105,'dilnawaj', 90.90)")
cursor.execute("update stud_tab set stud_marks=95 where stud_id=103")
cursor.execute("delete from stud_tab where stud_id=101")
cursor.execute("commit")
cursor.execute("select * from stud_tab")
rows=cursor.fetchone()
while rows is not None:
    print(rows)
    rows=cursor.fetchone()
cursor.close()
conn.close()


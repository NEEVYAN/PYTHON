# FIRST SETUP MYSQL AND INSTALL MYSQL CONNECTOR 
# ========================================================

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="1455R@j198",database="neeraj")

if mydb.is_connected():
    print("connection done")
    
mycursor=mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)
    
# ('information_schema',)
# ('mysql',)
# ('neeraj',)
# ('performance_schema',)
# ('sys',)
# ===========================================================

mycursor.execute("select * from student")
for i in mycursor:
    print(i)
    
# or 

# result=mycursor.fetchall()
# for i in result:
#     print(i)

# ('mmmut', 'student')
# ('anoara', 'fb')
# ===========================================================


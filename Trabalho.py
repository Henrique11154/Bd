import mysql.connector

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)

cursor = mydb.cursor()

cursor.execute (f'SELECT TABLE_NAME 
FROM ')

myresults = cursor.fetchall()

i = 0

for registro in myresult :
    print(f"{registro[i]}")
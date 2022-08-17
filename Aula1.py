import mysql.connector

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)

print("Digite um pais:")
nome = input()

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Customers where Country like '%" +nome+ "%' ")

myresult = mycursor.fetchall()

for registro in myresult:
    print(registro)
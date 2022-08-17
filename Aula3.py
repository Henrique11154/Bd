import mysql.connector

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)

print("Escolha uma tabela a ser consultada")
print("1 - Customers (clientes)")
print("2 - Employees (Empregados)")
print("3 = Orders (Compras)")
opcao = input()

if (opcao == '1'):
    tabela = "Customers"
    coluna = "ContactName"
    print("Digite um nome a ser pesquisado:")
    nome = input()

if(opcao == '2'):
    tabela = "Employees"
    coluna = "FirstName"
    print("Digite um nome a ser pesquisado:")

if(opcao == '3'):
    tabela = "Orders"
    

mycursor = mydb.cursor()

mycursor.execute(f'SELECT * FROM {tabela} where {coluna} like "%{nome}%"')

myresult = mycursor.fetchall()

for registro in myresult:
    print(registro)
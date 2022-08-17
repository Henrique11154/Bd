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
print("3 - Orders (Compras)")
print("4 - Suppliers (Fornecedor)")
print("5 - Products (produtos)")
print("6 - Shippers")
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
    nome = input()

if(opcao == '3'):
    tabela = "Orders"
    coluna = "CustomerID"
    nome = input()

if(opcao == '4'):
    tabela = "Suppliers"
    coluna = "CompanyName"
    print("Digite um nome a ser pesquisado:")
    nome = input()

if(opcao == '5'):
    tabela = "Products"
    coluna = "ProductName"
    print("Digite um nome a ser pesquisado:")
    nome = input()

if (opcao == '6'):
    tabela = "Shippers"
    coluna = "CompanyName"
    print("Digite um nome a ser pesquisado:")
    nome = input()
    

mycursor = mydb.cursor()

mycursor.execute(f"SELECT * FROM {tabela} where {coluna} like '%{nome}%'")

myresult = mycursor.fetchall()

for registro in myresult:
    print(registro)
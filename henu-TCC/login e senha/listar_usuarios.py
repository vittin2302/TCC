import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuario")

usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conexao.close()
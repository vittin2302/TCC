import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

nome = "vitor"
senha = "1234"

cursor.execute(
    "SELECT * FROM usuario WHERE nome = ? AND senha = ?",
    (nome, senha)
)

resultado = cursor.fetchone()

print(resultado)
if resultado:
    print("Login Correto")
else:
    print("Login Incorreto")

conexao.close()
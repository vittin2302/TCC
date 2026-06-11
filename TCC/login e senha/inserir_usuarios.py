import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO usuario (nome, senha) VALUES (?, ?)",
    ("vitor", "1234")
)

conexao.commit()
conexao.close()

print("Usuário cadastrado!")
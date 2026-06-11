import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute(
    "DELETE FROM usuario"
)

conexao.commit()
conexao.close()

print("Usuário excluido!")
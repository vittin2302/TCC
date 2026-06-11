import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    senha TEXT
)
""")

cursor.execute("""CREATE TABLE historia(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    sinopse TEXT
)
""")

conexao.commit()
conexao.close()

print("Banco criado com sucesso!")
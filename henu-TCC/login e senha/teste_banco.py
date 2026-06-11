import sqlite3
import os

print("Diretório atual:")
print(os.getcwd())

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

conexao.close()
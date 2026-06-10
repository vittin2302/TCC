from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        print("usuario digitado:", usuario)
        print("senha digitado:", senha)

        cursor.execute(
            "SELECT * FROM usuario WHERE nome = ? AND senha = ?",
            (usuario, senha)
        )

        resultado = cursor.fetchone()

        conexao.close()

        if resultado:
            return render_template("index.html")
        else:
            return "Usuário ou senha incorretos."

    return render_template("login.html")

@app.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        cursor.execute(
            ("SELECT * FROM usuario WHERE nome = ?"),
            (usuario,)
        )

        usuario_existe = cursor.fetchone()

        if usuario_existe:
            conexao.close()
            return f"Usuario {usuario} já é usado"

        cursor.execute(
            ("INSERT INTO usuario (nome, senha) VALUES (?, ?)"),
            (usuario, senha)
        )

        conexao.commit()
        conexao.close()
        
        return redirect("/")
    
    return render_template("cadastro.html")

app.run(debug=True)
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
            return redirect("/index")
        else:
            return redirect("/")

    return render_template("login.html")

@app.route("/esqueci", methods=["POST", "GET"])
def esqueci():
    if request.method == "POST":

        usuario = request.form["usuario"]
        nova_senha = request.form["senha"]

        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM usuario WHERE nome = ?",
            (usuario,)
        )

        resultado = cursor.fetchone()

        if not resultado:
            conexao.close()
            return "Usuário não encontrado"

        cursor.execute(
            "UPDATE usuario SET senha = ? WHERE nome = ?",
            (nova_senha, usuario)
        )

        conexao.commit()
        conexao.close()

        return redirect("/")

    return render_template("esqueci.html")

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

@app.route("/biblioteca")
def biblioteca():

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM historia")

    historias = cursor.fetchall()

    conexao.close()

    return render_template(
        "biblioteca.html",
        historias=historias
    )
    


@app.route("/comunidade")
def comunidade():
    return render_template("comunidade.html")


@app.route("/confirmar-publicacao")
def confirmar_publicacao():
    return render_template("confirmar-publicacao.html")


@app.route("/informacoes-livro", methods=["GET", "POST"])
def informacoes_livro():

    if request.method == "POST":

        titulo = request.form["titulo"]
        sinopse = request.form["sinopse"]

        conexao = sqlite3.connect("banco.db")
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO historia (titulo, sinopse) VALUES (?, ?)",
            (titulo, sinopse)
        )

        conexao.commit()
        conexao.close()

        return redirect("/confirmar-publicacao")

    return render_template("informacoes-livro.html")


@app.route("/publicar-historia")
def publicar_historia():
    return render_template("publicar-historia.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/index")
def index():
    return render_template("index.html")

app.run(debug=True)
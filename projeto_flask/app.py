from flask import Flask, render_template, request, redirect, url_for

def obter_produtos():
    with open("produtos.csv", "r") as file:
        lista_produtos = []
        linhas = file.readlines()
        for linha in linhas:
            nome, descricao, preco, imagem = linha.strip().split(",")
            produto = {
                "nome": nome,
                "descricao": descricao,
                "preco": preco,
                "imagem": imagem
            }
            lista_produtos.append(produto)
        return lista_produtos
    
def adicionar_produto(p):
    with open("produtos.csv", "a") as file:
        linha = f"\n{p['nome']},{p['descricao']},{p['preco']},{p['imagem']}"
        file.write(linha)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=obter_produtos())

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in obter_produtos():
        if produto["nome"] == nome:
            return render_template("produto.html", produto=produto)

#GET
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

#POST
@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']
    produto = {"nome": nome,
               "descricao": descricao,
               "preco": preco,
               "imagem": imagem}
    adicionar_produto(produto)

    return redirect(url_for("produtos"))


app.run()
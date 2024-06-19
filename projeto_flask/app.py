from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
    {"nome": "coca-cola", "descricao": "veneno", "preco": "R$4", "imagem": "https://coca-colafemsa.com/wp-content/uploads/2022/03/CC-botella-237-zero-2018-digital.webp"},
    {"nome": "doritos", "descricao": "suja mão", "preco": "R$8", "imagem": "https://m.media-amazon.com/images/I/51CmkuCoLoL._AC_SL1000_.jpg"},
    {"nome": "agua", "descricao": "mata sede", "preco": "R$2", "imagem": "https://io.convertiez.com.br/m/superpaguemenos/shop/products/images/15890/medium/agua-mineral-crystal-sem-gas-500ml_89544.png"},
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
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
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))


app.run()
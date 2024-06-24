from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ


app = Flask(__name__)
cnpj = CNPJ()
cpf = CPF()

@app.route("/")
def home():
    return render_template("gerar-cnpj.html", cnpj=cnpj)

@app.route("/gerar-cnpj")
def gerar_cnpj():
    return render_template("gerar-cnpj.html", cnpj=cnpj)

@app.route("/gerar-cpf")
def gerar_cpf():
    return render_template("gerar-cpf.html", cpf=cpf)

#GET
@app.route("/validar-cnpj")
def validar_cnpj():
    return render_template("validar-cnpj.html", cnpj=cnpj)

#GET
@app.route("/validar-cpf")
def validar_cpf():
    return render_template("validar-cpf.html", cpf=cpf)

#POST
@app.route("/resultado-cnpj", methods=["POST"])
def resultado_cnpj():
    cnpj_informado = request.form['cnpj']
    validacao = cnpj.validate(cnpj_informado)
    return render_template("resultado-cnpj.html", cnpj_informado=cnpj_informado, validacao=validacao)

#POST
@app.route("/resultado-cpf", methods=["POST"])
def resultado_cpf():
    cpf_informado = request.form['cpf']
    validacao = cpf.validate(cpf_informado)
    return render_template("resultado-cpf.html", cpf_informado=cpf_informado, validacao=validacao)


app.run()
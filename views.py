from flask import render_template, request, redirect, url_for
from flask_app import app
from models import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/clientes')
def clientes():
    clientes = Clientes.lista_clientes()
    return render_template('clientes.html', clientes = clientes)

@app.route('/cliente-detalhes/<int:id>')
def cliente_detalhes(id):
    cliente = Clientes.busca_cliente(id)
    return render_template('cliente-detalhes.html', cliente = cliente)

@app.route('/cliente-novo')
def cliente_novo():
    return render_template('cliente-novo.html')

@app.route('/cliente-cadastrar', methods=['POST',])
def cliente_cadastrar():
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    Clientes.cadastra_cliente(nome, telefone, email)
    return redirect(url_for('clientes'))

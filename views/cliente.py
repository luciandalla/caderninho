from flask import render_template, request, redirect, url_for
from flask_app import app
from models.clientes import *
from models.lancamentos import *

@app.route('/clientes')
def clientes():
    clientes = Clientes.lista_clientes()
    return render_template('clientes.html', clientes = clientes)

@app.route('/cliente-detalhes/<int:id>')
def cliente_detalhes(id):
    cliente = Clientes.busca_cliente(id)
    lancamentos = Lancamentos.busca_lancamentos(id)
    return render_template('cliente-detalhes.html', cliente = cliente, lancamentos=lancamentos)

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

@app.route('/cliente-editar/<int:id>')
def cliente_editar(id):
    cliente = Clientes.busca_cliente(id)
    return render_template('cliente-editar.html', cliente=cliente)

@app.route('/cliente-atualizacao/', methods=['POST',])
def cliente_atualizacao():
    id = request.form['id']
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    Clientes.alterar_cliente(id, nome, telefone, email)
    cliente = Clientes.busca_cliente(id)
    return render_template('cliente-detalhes.html', cliente = cliente)

@app.route('/cliente-excluir/<int:id>')
def cliente_excluir(id):
    Clientes.excluir_cliente(id)
    return redirect(url_for('clientes'))
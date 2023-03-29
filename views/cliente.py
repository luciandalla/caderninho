from flask import render_template, request, redirect, url_for, session
from flask_app import app
from models.clientes import *
from models.lancamentos import *
from models.pagamentos import *

@app.route('/clientes')
def clientes():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    usuario = session['usuario']
    clientes = Clientes.lista_clientes()
    return render_template('clientes.html', clientes = clientes, usuario=usuario)

@app.route('/cliente-detalhes/<int:id>')
def cliente_detalhes(id):
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    cliente = Clientes.busca_cliente(id)
    lancamentos = Lancamentos.busca_lancamentos(id)
    pagamentos = Pagamentos.busca_pagamentos(id)
    return render_template('cliente-detalhes.html', cliente = cliente, lancamentos=lancamentos, pagamentos=pagamentos)

@app.route('/cliente-novo')
def cliente_novo():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    return render_template('cliente-novo.html')

@app.route('/cliente-cadastrar', methods=['POST',])
def cliente_cadastrar():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    Clientes.cadastra_cliente(nome, telefone, email)
    return redirect(url_for('clientes'))

@app.route('/cliente-editar/<int:id>')
def cliente_editar(id):
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    cliente = Clientes.busca_cliente(id)
    return render_template('cliente-editar.html', cliente=cliente)

@app.route('/cliente-atualizacao/', methods=['POST',])
def cliente_atualizacao():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    id = request.form['id']
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    Clientes.alterar_cliente(id, nome, telefone, email)
    return redirect(url_for('cliente_detalhes', id=id))

@app.route('/cliente-excluir/<int:id>')
def cliente_excluir(id):
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    Clientes.excluir_cliente(id)
    return redirect(url_for('clientes'))
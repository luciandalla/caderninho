from flask import render_template, request, redirect, url_for
from flask_app import app
from models.clientes import *
from models.lancamentos import *

@app.route('/lancamento-novo/<int:id>')
def lancamento_novo(id):
    cliente = Clientes.busca_cliente(id)
    return render_template('lancamento-novo.html', cliente=cliente)

@app.route('/lancamento-cadastrar', methods=['POST',])
def lancamento_cadastrar():
    data = request.form['data']
    valor = request.form['valor']
    observacao = request.form['observacao']
    cliente_id = request.form['cliente_id']
    Lancamentos.cadastra_lancamento(data, valor, observacao, cliente_id)
    return redirect(url_for('cliente_detalhes', id=cliente_id))

@app.route('/lancamento-editar/<int:id>')
def lancamento_editar(id):
    lancamento = Lancamentos.busca_lancamento(id)
    return render_template('lancamento-editar.html', lancamento=lancamento)

@app.route('/lancamento-atualizacao/', methods=['POST',])
def lancamento_atualizacao():
    id = request.form['id']
    data = request.form['data']
    valor = request.form['valor']
    observacao = request.form['observacao']
    cliente_id = request.form['cliente_id']
    Lancamentos.altera_lancamento(id, data, valor, observacao, cliente_id)
    return redirect(url_for('cliente_detalhes', id=cliente_id))

@app.route('/lancamento-excluir/<int:id>')
def lancamento_excluir(id):
    lancamento = Lancamentos.busca_lancamento(id)
    Lancamentos.excluir_lancamento(id)
    return redirect(url_for('cliente_detalhes', id=lancamento.id_cliente))
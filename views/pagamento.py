from flask import render_template, request, redirect, url_for
from flask_app import app
from models.pagamentos import *

@app.route('/pagamento-novo/<int:id>')
def pagamento_novo(id):
    cliente = Clientes.busca_cliente(id)
    return render_template('pagamento-novo.html', cliente=cliente)

@app.route('/pagamento-cadastrar', methods=['POST',])
def pagamento_cadastrar():
    data = request.form['data']
    valor = request.form['valor']
    observacao = request.form['observacao']
    cliente_id = request.form['cliente_id']
    Pagamentos.cadastra_pagamento(data, valor, observacao, cliente_id)
    return redirect(url_for('cliente_detalhes', id=cliente_id))

@app.route('/pagamento-editar/<int:id>')
def pagamento_editar(id):
    pagamento = Pagamentos.busca_pagamento(id)
    return render_template('pagamento-editar.html', pagamento=pagamento)

@app.route('/pagamento-atualizacao/', methods=['POST',])
def pagamento_atualizacao():
    id = request.form['id']
    data = request.form['data']
    valor = request.form['valor']
    observacao = request.form['observacao']
    cliente_id = request.form['cliente_id']
    Pagamentos.altera_pagamento(id, data, valor, observacao, cliente_id)
    return redirect(url_for('cliente_detalhes', id=cliente_id))

@app.route('/pagamento-excluir/<int:id>')
def pagamento_excluir(id):
    pagamento = Pagamentos.busca_pagamento(id)
    Pagamentos.excluir_pagamento(id)
    return redirect(url_for('cliente_detalhes', id=pagamento.id_cliente))
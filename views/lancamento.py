from flask import render_template, request, redirect, url_for, session
from flask_app import app
from models.lancamentos import *

@app.route('/lancamento-novo/<int:id>')
def lancamento_novo(id):
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    cliente = Clientes.busca_cliente(id)
    return render_template('lancamento-novo.html', cliente=cliente)

@app.route('/lancamento-cadastrar', methods=['POST',])
def lancamento_cadastrar():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    data = request.form['data']
    valor = request.form['valor']
    observacao = request.form['observacao']
    cliente_id = request.form['cliente_id']
    Lancamentos.cadastra_lancamento(data, valor, observacao, cliente_id)
    return redirect(url_for('cliente_detalhes', id=cliente_id))

@app.route('/lancamento-editar/<int:id>')
def lancamento_editar(id):
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    lancamento = Lancamentos.busca_lancamento(id)
    return render_template('lancamento-editar.html', lancamento=lancamento)

@app.route('/lancamento-atualizacao/', methods=['POST',])
def lancamento_atualizacao():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    id = request.form['id']
    data = request.form['data']
    valor = request.form['valor']
    observacao = request.form['observacao']
    cliente_id = request.form['cliente_id']
    Lancamentos.altera_lancamento(id, data, valor, observacao, cliente_id)
    return redirect(url_for('cliente_detalhes', id=cliente_id))

@app.route('/lancamento-excluir/<int:id>')
def lancamento_excluir(id):
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    lancamento = Lancamentos.busca_lancamento(id)
    Lancamentos.excluir_lancamento(id)
    return redirect(url_for('cliente_detalhes', id=lancamento.id_cliente))
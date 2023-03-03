from flask import render_template
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
    cliente = Clientes.detalha_cliente(id)
    return render_template('cliente-detalhes.html', cliente = cliente)

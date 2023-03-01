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

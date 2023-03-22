from flask import render_template, session, redirect, url_for
from flask_app import app
from models.lancamentos import Lancamentos
from models.pagamentos import Pagamentos
from models.clientes import Clientes

def total_a_receber():
    total_lancamentos = Lancamentos.soma_total_lancamentos()
    total_pagamentos = Pagamentos.soma_total_pagamentos()
    total = total_lancamentos - total_pagamentos
    return total

@app.route('/')
def home():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))

    valores_a_receber = total_a_receber()

    return render_template('home.html', valores_a_receber=valores_a_receber)


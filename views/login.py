from flask import render_template, request, redirect, url_for, session, flash
from flask_app import app
from models.usuarios import *

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login-autenticar', methods=['POST',])
def login_autenticar():
    usuario_digitado = request.form['usuario']
    senha_digitada = request.form['senha']
    usuario = Usuarios.existe_usuario(usuario_digitado)

    if (usuario):
        if (senha_digitada == usuario.senha):
             session['usuario'] = usuario.usuario
             return redirect(url_for('home'))
        else:
             flash('Usuário e/ou senha inválidos!')
             return redirect(url_for('login'))
    else:
        flash('Usuário e/ou senha inválidos!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout ():
    session['usuario'] = None
    return redirect(url_for('login'))
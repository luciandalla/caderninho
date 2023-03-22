from flask import render_template, session, redirect, url_for
from flask_app import app


@app.route('/')
def home():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login'))
    return render_template('home.html')

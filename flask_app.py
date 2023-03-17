from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from views.cliente import *
from views.lancamento import *
from views.pagamento import *
from views.gerais import *

if __name__ == '__main__':
    app.run(debug=True)
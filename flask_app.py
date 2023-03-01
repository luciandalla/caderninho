from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)
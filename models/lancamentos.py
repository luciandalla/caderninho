from flask_app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.clientes import Clientes


class Lancamentos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    observacao = db.Column(db.String(100), nullable=False)
    id_cliente = db.Column(db.Integer, ForeignKey('clientes.id'))
    clientes = relationship(Clientes)

    def __repr__(self):
        return '<Name %r>' % self.name

    @staticmethod
    def busca_lancamentos(cliente_id):
        lancamentos = Lancamentos.query.filter_by(id_cliente=cliente_id).order_by(Lancamentos.data)
        return lancamentos
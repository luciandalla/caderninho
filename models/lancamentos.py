from flask_app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.clientes import Clientes


class Lancamentos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    observacao = db.Column(db.String(100))
    id_cliente = db.Column(db.Integer, ForeignKey('clientes.id'))
    clientes = relationship(Clientes)

    def __repr__(self):
        return '<Name %r>' % self.name

    @staticmethod
    def busca_lancamento(id):
        lancamento = Lancamentos.query.filter_by(id=id).first()
        return lancamento

    @staticmethod
    def busca_lancamentos(cliente_id):
        lancamentos = Lancamentos.query.filter_by(id_cliente=cliente_id).order_by(Lancamentos.data)
        return lancamentos

    @staticmethod
    def busca_todos_lancamentos():
        lancamentos = Lancamentos.query.order_by(Lancamentos.data)
        return lancamentos

    @staticmethod
    def cadastra_lancamento(data, valor, observacao, cliente_id):
        lancamento = Lancamentos(data=data, valor=valor, observacao=observacao, id_cliente=cliente_id)
        db.session.add(lancamento)
        db.session.commit()
        return 'Lançamento cadastrado com sucesso!'

    @staticmethod
    def altera_lancamento(id, data, valor, observacao, cliente_id):
        lancamento = Lancamentos.busca_lancamento(id)
        lancamento.data = data
        lancamento.valor = valor
        lancamento.observacao = observacao
        lancamento.id_cliente = cliente_id
        db.session.add(lancamento)
        db.session.commit()
        mensagem = f"Lançamento foi alterado com sucesso!"
        return mensagem

    @staticmethod
    def excluir_lancamento(id):
            Lancamentos.query.filter_by(id=id).delete()
            db.session.commit()
            return "Lancamento deletado com sucesso!"

    @staticmethod
    def soma_total_lancamentos():
        total = 0
        lancamentos = Lancamentos.busca_todos_lancamentos()
        for lancamento in lancamentos:
            total = total + lancamento.valor
        return total

    @staticmethod
    def total_lancamentos_cliente(cliente_id):
        lancamentos = Lancamentos.busca_lancamentos(cliente_id)
        total = 0
        for lancamento in lancamentos:
            total = total + lancamento.valor
        return total
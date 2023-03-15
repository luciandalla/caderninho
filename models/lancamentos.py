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
    def busca_lancamento(id):
        lancamento = Lancamentos.query.filter_by(id=id).first()
        return lancamento

    @staticmethod
    def busca_lancamentos(cliente_id):
        lancamentos = Lancamentos.query.filter_by(id_cliente=cliente_id).order_by(Lancamentos.data)
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
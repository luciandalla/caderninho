from flask_app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.clientes import Clientes


class Pagamentos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    observacao = db.Column(db.String(100))
    id_cliente = db.Column(db.Integer, ForeignKey('clientes.id'))
    clientes = relationship(Clientes)

    def __repr__(self):
        return '<Name %r>' % self.name

    @staticmethod
    def busca_pagamento(id):
        pagamento = Pagamentos.query.filter_by(id=id).first()
        return pagamento

    @staticmethod
    def busca_pagamentos(cliente_id):
        pagamentos = Pagamentos.query.filter_by(id_cliente=cliente_id).order_by(Pagamentos.data)
        return pagamentos

    @staticmethod
    def cadastra_pagamento(data, valor, observacao, cliente_id):
        pagamento = Pagamentos(data=data, valor=valor, observacao=observacao, id_cliente=cliente_id)
        db.session.add(pagamento)
        db.session.commit()
        return 'Pagamento cadastrado com sucesso!'

    @staticmethod
    def altera_pagamento(id, data, valor, observacao, cliente_id):
        pagamento = Pagamentos.busca_pagamento(id)
        pagamento.data = data
        pagamento.valor = valor
        pagamento.observacao = observacao
        pagamento.id_cliente = cliente_id
        db.session.add(pagamento)
        db.session.commit()
        mensagem = f"Pagamento foi alterado com sucesso!"
        return mensagem

    @staticmethod
    def excluir_pagamento(id):
            Pagamentos.query.filter_by(id=id).delete()
            db.session.commit()
            return "Pagamento deletado com sucesso!"
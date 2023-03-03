from flask_app import db
from valida_dados import Validador

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

    @staticmethod
    def lista_clientes():
        clientes = Clientes.query.order_by(Clientes.nome)
        return clientes

    @staticmethod
    def busca_cliente(id):
        cliente = Clientes.query.filter_by(id=id).first()
        return cliente

    @staticmethod
    def cadastra_cliente(nome, telefone, email):

        nome_validado = Validador.valida_nome(nome)
        email_validado = Validador.valida_email(email)
        telefone_validado = Validador.valida_telefone(telefone)
        dados_validados = nome_validado and email_validado and telefone_validado

        if(dados_validados):
            cliente = Clientes(nome=nome.upper(), telefone=telefone, email=email.upper())
            db.session.add(cliente)
            db.session.commit()
            mensagem = f"Cliente {nome} for cadastrado com sucesso!"
        else:
            mensagem = "Não foi possível cadastrar o cliente!"

        return mensagem
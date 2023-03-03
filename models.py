from flask_app import db

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
    def detalha_cliente(id):
        cliente = Clientes.query.filter_by(id=id).first()
        return cliente
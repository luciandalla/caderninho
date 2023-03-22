from flask_app import db

class Usuarios(db.Model):
    usuario = db.Column(db.String(8), primary_key=True)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

    @staticmethod
    def existe_usuario(usuario):
        usuario = Usuarios.query.filter_by(usuario=usuario).first()
        if (usuario):
            return usuario
        else:
            return False


SECRET_KEY = 'caderninho'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'Fr3a8xsee',
        servidor = 'localhost',
        database = 'caderninho'
    )
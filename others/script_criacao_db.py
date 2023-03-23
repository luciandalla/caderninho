import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Fr3a8xsee'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `caderninho`;")

cursor.execute("CREATE DATABASE `caderninho`;")

cursor.execute("USE `caderninho`;")

TABLES = {}

# TABELAS

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `usuario` varchar(8) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`usuario`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Clientes'] = ('''
      CREATE TABLE `clientes` (
      `id` int(8) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `telefone` varchar(20) NOT NULL,
      `email` varchar(70) NOT NULL,
      `saldo` float NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Lancamentos'] = ('''
      CREATE TABLE `lancamentos` (
      `id` int(8) NOT NULL AUTO_INCREMENT,
      `data` date NOT NULL,
      `valor` float NOT NULL,
      `observacao` varchar(100),
      `id_cliente` integer NOT NULL,
      PRIMARY KEY (`id`),
      CONSTRAINT fk_UserLancamento FOREIGN KEY (id_cliente) REFERENCES Clientes (id)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Pagamentos'] = ('''
      CREATE TABLE `pagamentos` (
      `id` int(8) NOT NULL AUTO_INCREMENT,
      `data` date NOT NULL,
      `valor` float NOT NULL,
      `observacao` varchar(100),
      `id_cliente` integer NOT NULL,
      PRIMARY KEY (`id`),
      CONSTRAINT fk_UserPagamento FOREIGN KEY (id_cliente) REFERENCES Clientes (id)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')

# DADOS INICIAIS

usuario_sql = 'INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)'
usuarios = [
      ("admin", "admin")
]
cursor.executemany(usuario_sql, usuarios)

conn.commit()
cursor.close()
conn.close()

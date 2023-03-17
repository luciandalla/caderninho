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

TABLES['Clientes'] = ('''
      CREATE TABLE `clientes` (
      `id` int(8) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `telefone` varchar(20) NOT NULL,
      `email` varchar(70) NOT NULL,
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

cliente_sql = 'INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)'
clientes = [
    ("LUCIAN MACIEL", "51994652141", "LUCIAN@GMAIL.COM")
]
cursor.executemany(cliente_sql, clientes)

lancamento_sql = 'INSERT INTO lancamentos (data, valor, observacao, id_cliente) VALUES (%s, %s, %s, %s)'
lancamentos = [
    ("2023-03-09", "250", "Compra de relógio de pulso", "1")
]
cursor.executemany(lancamento_sql, lancamentos)

pagamento_sql = 'INSERT INTO pagamentos (data, valor, observacao, id_cliente) VALUES (%s, %s, %s, %s)'
pagamentos = [
    ("2023-03-12", "150", "Pagamento via Pix", "1")
]
cursor.executemany(pagamento_sql, pagamentos)

conn.commit()
cursor.close()
conn.close()

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
    ("LUCIAN MACIEL", "51994652141", "LUCIAN@GMAIL.COM"),
    ("BARBARA BECKER", "51958744741", "BARBARA_B@HOTMAIL.COM"),
]
cursor.executemany(cliente_sql, clientes)

conn.commit()
cursor.close()
conn.close()

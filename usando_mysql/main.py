# PyMySql - um cliente MySQL feito em Python puro
# Cliente é o cara que vai conectar no servidor e vai realizar as queries

# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

# Python não vem com servidor MySQL, então teremos que instala-lo
# pip install pymysql

# Por ser em Python puro, ele possui context-manager, diferentemente do sqlite3

# Geralmente não criamos tabelas, utilizamos algumas prontas e renomadsa
# Jusatamente pelo MySQL tratar de grandes dados

import os

import dotenv
import pymysql

dotenv.load_dotenv()

TABLE_NAME = "customers"

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],  # qual servidor vou conectar
    user=os.environ['MYSQL_USER'],  # qual o usuario
    password=os.environ['MYSQL_PASSWORD'],  # qual a senha do usuario
    database=os.environ['MYSQL_DATABASE'],  # qual a base de dados
)

# cursor = connection.cursor()
# cursor.close()       não é necessário, pois temos context manager
# connection.close()

# print(os.environ['MYSQL_DATABASE'])

with connection:
    with connection.cursor() as cursor:
        # Minha query sql vem aqui
        cursor.execute(
            # Comando create nao precisa de commit
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '  # varchar-string limitavel(50)char
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        # TRUNCATE limpa a tabela inteira
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        # connection.commit() não pode ser usado no método CREATE

    # Posso usar varios cursores na mesma conexão
    with connection.cursor() as cursor:
        # result = cursor.execute(texto) atribuir em uma var me mostra
        # quantas linhas foram afetadas com o comando, posso utilizar SELECT
        # também
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Carlos", 16) '
        )
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Tinha", 3) '
        )
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("Fabiano", 5) '
        )
        connection.commit()  # NÃO ESQUEÇA de commitar

    # Evitando SQL injection
    # Passando assim, os valores são codificados e não são passados como
    # Comandos SQL
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%s, %s) '
        )
        data = ("Carlos placeholder", 30)
        cursor.execute(sql, data)
        connection.commit()

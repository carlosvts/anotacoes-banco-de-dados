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
    # CRUD
    # C - Create
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
        data = ("Carlos placeholder", 30)  # Teria que seguir a ordem dos place
        cursor.execute(sql, data)
        connection.commit()

    # Inserindo valores com dicionários ao invés de iteráveis
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%(name)s, %(age)s) '  # agora os places
            # tem que bater com a ordem (nome, idade), que
            # é a ordem das colunas
            # o nome dos placeholders DEVEM BATER com o nome das chaves
            # do dicionário
        )
        data_dict = {
            "age": 25,  # a ordem do dict é irrelevante
            "name": "Carlos dict",

        }
        cursor.execute(sql, data_dict)
        connection.commit()

    # Utilizando executemany, os argumentos devem ser iteráveis
    # Pode ser um iterável com dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%(name)s, %(age)s) '
        )

        data_iteravel_dict = (
            {"age": 46, "name": "Carlos iteravel 1"},
            {"age": 47, "name": "Carlos iteravel 2"},
            {"age": 48, "name": "Carlos iteravel 3"},
        )
        cursor.executemany(sql, data_iteravel_dict)  # mandando vários dados
        connection.commit()

    # Mas pode ser um iterável de iteráveis, uma tupla de tuplas por exemplo
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%s, %s) '  # Agora é preciso alterar aqui
        )  # Além de que preciso manter a ordem

        data_iteravel_2 = (
            ("Carlos tupla 1", 53),
            ("Carlos tupla 2", 54)
        )
        cursor.executemany(sql, data_iteravel_2)  # mandando vários dados
        connection.commit()

    # CRUD
    # R - Read, lendo valores com SELECT
    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '  # selecione tudo da customers
            'WHERE id = 3 '  # ou where id > 3, posso fazer varias coisas
        )
        cursor.execute(sql)  # com SELECT não preciso commitar nada
        # cursor.mogrify

        # Eles são iterators, ou seja, esgotam
        dados_coletados = cursor.fetchall()

        # for row in dados_coletados:
        #     print(row)

    # Utilizando input e calculadamente evitando SQL injection
    with connection.cursor() as cursor:
        menor_id = int(input('Digite o menor id: '))
        maior_id = int(input('Digite o maior id: '))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s  '
        )
        cursor.execute(sql)  # type: ignore

        cursor.execute(sql, (menor_id, maior_id))  # type: ignore
        print(cursor.mogrify(sql, (menor_id, maior_id)))  # type: ignore
        data5 = cursor.fetchall()  # type: ignore

        # for row in data5:
        #     print(row)

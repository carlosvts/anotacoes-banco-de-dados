# PyMySql - um cliente MySQL feito em Python puro
# Cliente é o cara que vai conectar no servidor e vai realizar as queries

# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

# Python não vem com servidor MySQL, então teremos que instala-lo
# pip install pymysql

# Por ser em Python puro, ele possui context-manager, diferentemente do sqlite3

import os

import dotenv
import pymysql

dotenv.load_dotenv()

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
        print(cursor)

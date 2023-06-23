# SQLite3: forma de organizar, remover e estruturar dados
# SQLite3 não é utilizado em grande escala, por isso "lite"
# Ele é bom para uso em pequena escala, como se fosse um JSON parrudo
# Para coisas em larga escala, MySQL é recomendado
# O SQLite3 já vem com o python, não é necessário instalação

# Como geralmente funciona:
# Sevidor -> base de dados -> tabelas
# servidor tem base de dados que tem tabelas com informações(colunas)
# dentro das colunas teremos valores

# CREATE - cria coisas
# INSERT - adiciona coisas
# SELECT - ver coisas
# DELETE - deleta
# DELETE com where -
# DELETE sem where -

# CRUD -  Create Read   Update Delete
# no SQL- INSERT SELECT UPDATE DELETE

# Doc: https://www.sqlite.org/doclist.html

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

if __name__ == "__main__":
    # ABRINDO
    # Geralmente a variavel é abreviada para con, sqlite3.connect retorna uma
    # classe
    connection = sqlite3.connect(DB_FILE)

# O que vai executar e administrar (query) na base de dados
# O cursor se esgota depois de utiliza-lo para pegar valores, não para enviar
    cursor = connection.cursor()

# SQL

# cursor.execute(  # É necessário olhar a documentação para saber os comandos
#     f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
#     '('
#     'id INTEGER PRIMARY KEY AUTO INCREMENT,' # PRIMARY KEY é tipo um índice
#                                          utilizamos ela para achar os valores
#     'name TEXT,'  # TEXT é str em SQL
#     'weight REAL'  # REAL é float em SQL
#     ')'  # O que estamos fazendo aqui é enviando parametros para a db
# )  # mas estamos fazendo isso utilizando a linguagem dela (SQL)


# Cuidado: fazendo delete sem where (where é onde passamos o ID)
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )
# connection.commit() # mesmo deletando a tabela inteira, os IDS continuam
# fazendo a sua contagem

# PARA DELETAR OS ID's
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )

# CRIA TABELA
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'name TEXT,'
        'weight REAL'
        ')'
    )
    connection.commit()  # Envia as mudanças executadas, 'commita' ela

# Adicionando valores nas colunas da tabela
# Cuidado: SQL Injection
    cursor.execute(
        f'INSERT INTO {TABLE_NAME} (id, name, weight) '
        'VALUES (NULL, "Carlos Vinícius", 9.9)'
    )
# connection.commit()  # Enviando novamente as mudanças


# executemany - PASSA VARIOS VALORES
# cursor.executemany(
#     f'INSERT INTO {TABLE_NAME} (name, weight) '
#     'VALUES (?, ?)', [['Tinha', 3], ['Fabiano', 5]]
# )


# execute com dicionário
    cursor.execute(
        f'INSERT INTO {TABLE_NAME} (name, weight) '
        'VALUES (:name, :weight)', {'name': "Tinha", "weight": 3}
    )

# executemany com dicionário
    values = (
        {'name': 'Tinha', 'weight': 3},
        {'name': 'Fabiano', 'weight': 5},
        {'name': 'de Souza', 'weight': 16},
    )

    for value in values:
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} (name, weight) '
            'VALUES (:name, :weight)', value)
    connection.commit()

# NÃO ESQUEÇA DE FECHAR
    connection.close()
    cursor.close()

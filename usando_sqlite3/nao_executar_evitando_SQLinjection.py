# NÃO EXECUTAR ESTE CÓDIGO
# forma de como evitar uma sqlinjection, colocando placeholders
# sql injection -  quando seu sistema é vulnerável o suficiente para
# alguem através de uma injeção de um possível nome ou peso acaba, nesse caso
# injetando um comando que copia sua tabela ou que deleta-a

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

# cursor.execute(
#     f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
#     '('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#     'name TEXT,'
#     'weight REAL'
#     ')'
# )
# con.commit()

# A melhor maneira de passar valores
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES (?, ?)',  # poderia ser placeholder, params, etc
    ['Carlos Vinícius', '23']  # Esses são os parametros dos dois interrogações
)
con.commit()

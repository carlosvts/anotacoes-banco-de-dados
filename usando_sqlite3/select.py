# Fazendo consultas e seleções de dados
import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Selecione tudo da table_name e limita 2
cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT 2')
# posso usar LIMIT ou  WHERE id = "3"

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)


connection.close()
cursor.close()

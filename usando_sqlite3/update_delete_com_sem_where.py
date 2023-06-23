# DELETE - Deleta
# Delete sem where, não especifica o que é para ser deletado
# então há chance de você apagar sua bbase de dados inteira
#
# Delete com where, especifica onde vai ser deletado e, com isso
# o mecanismo fica bem mais seguro
# DELETE E UPDATE DEVEM TER WHERE


import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id="12"')  # deleta o id 10
connection.commit()

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET weight="5", name="Tinhudo" '
    'WHERE id="20" '
)
connection.commit()

connection.close()
cursor.close()

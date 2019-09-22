import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.execute('SELECT * FROM clientes_cliente')
cursor.description
colnames = cursor.description
for row in colnames:
    print(row[0])
conn.close()
import sqlite3

#ALTERANDO TABELA

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
ALTER TABLE clientes_cliente ADD dt_nascimento DATE;
""")
conn.close()



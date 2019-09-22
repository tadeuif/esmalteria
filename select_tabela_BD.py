import sqlite3

#SELECIONANDO ITENS DA TABELA

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM clientes_cliente;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()

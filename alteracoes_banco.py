import sqlite3

# conectando...
#conn = sqlite3.connect('db.sqlite3')
## definindo um cursor
#cursor = conn.cursor()

# criando a tabela (schema)
'''cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
);
""")'''

#print('Tabela criada com sucesso.')

# desconectando...
#conn.close()

#terminal sqlite3 db.sqlite3.db 'PRAGMA table_info(db.sqlite3)'

#SELECIONANDO ITENS DA TABELA
'''
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM clientes_cliente;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
'''

#ALTERANDO TABELA

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
ALTER TABLE clientes_cliente ADD dt_nascimento DATE;
""")

conn.close()
'''
#VENDO AS COLUNAS

conn = sqlite3.connect('db.sqlite3')
cursor = conn.execute('SELECT * FROM clientes_cliente')
cursor.description
colnames = cursor.description
for row in colnames:
    print(row[0])
conn.close()
'''
import sqlite3

# conectando...
conn = sqlite3.connect('db.sqlite3')
## definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE agendamento (
        id                      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome                    TEXT NOT NULL,
        tipo                    TEXT NOT NULL,
        descricao               TEXT NOT NULL,
        preco                   FLOAT NOT NULL,
        produto                 TEXT NOT NULL,
        disponibilidade         BIT NOT NULL,
        tm_execucao             TIME NOT NULL,
        pco_venda               FLOAT NOT NULL
);
""")

print('Tabela criada com sucesso.')

# desconectando...
conn.close()
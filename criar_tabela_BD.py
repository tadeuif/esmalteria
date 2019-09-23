import sqlite3

# conectando...
conn = sqlite3.connect('db.sqlite3')
## definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute(
CREATE TABLE pagamento (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cod_servico        TEXT NOT NULL,
        cod_cliente        TEXT NOT NULL,
        valor_pagamento    TEXT NOT NULL,
        dt_pagamento       TEXT NOT NULL,
        status             TEXT NOT NULL
);
)

print('Tabela criada com sucesso.')

# desconectando...
conn.close()
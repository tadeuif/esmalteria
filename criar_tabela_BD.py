import sqlite3

# conectando...
conn = sqlite3.connect('db.sqlite3')
## definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute(
CREATE TABLE agendamento_agendamento (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome    TEXT NOT NULL,
        dt_agendamento    TEXT NOT NULL,
        hora_agendamento    TEXT NOT NULL,
        servico_prestado TEXT NOT NULL
);
)

print('Tabela criada com sucesso.')

# desconectando...
conn.close()
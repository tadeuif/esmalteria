import sqlite3

# conectando...
conn = sqlite3.connect('db.sqlite3')
## definindo um cursor
cursor = conn.cursor()

#DROPANDO TABELA
cursor.execute("DROP TABLE agendamento_agendamento")

print('Tabela dropada com sucesso.')

# desconectando...
conn.close()
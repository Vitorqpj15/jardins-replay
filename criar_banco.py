import sqlite3

conn = sqlite3.connect("pelada.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS lances (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_arquivo TEXT NOT NULL,
        data_hora TEXT NOT NULL
    )
""")

conn.commit()
conn.close()

print("Banco de dados criado e verificado com sucesso!")
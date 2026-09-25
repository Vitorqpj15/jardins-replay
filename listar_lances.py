import sqlite3 

conn = sqlite3.connect("pelada.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Lances")
resultados = cursor.fetchall()

if not resultados:
    print("Nenhum lance encontrado no banco de dados.")
else: 
    for linha in resultados: 
        id_lance, nome_arquivo, data_hora = linha
        (print(f"[{id_lance}] {nome_arquivo} - gravado em {data_hora}"))

conn.close()
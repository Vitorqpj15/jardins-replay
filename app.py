from flask import Flask, send_from_directory
import sqlite3

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    conn = sqlite3.connect("pelada.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome_arquivo, data_hora FROM lances ORDER BY id DESC")
    lances = cursor.fetchall()
    conn.close()

    html = "<h1>Pelada Replay</h1>"

    if not lances:
        html += "<p>Nenhum lance registrado ainda.</p>"
    else:
        for nome_arquivo, data_hora in lances:
            
            nome_sem_pasta = nome_arquivo.replace("lances/", "")
            html += f"""
                <div>
                    <p>Lance gravado em {data_hora}</p>
                    <video width="480" controls>
                        <source src="/lances/{nome_sem_pasta}" type="video/mp4">
                    </video>
                </div>
                <hr>
            """

    return html

@app.route("/lances/<nome_arquivo>")
def servir_video(nome_arquivo):
    return send_from_directory("lances", nome_arquivo)

if __name__ == "__main__":
    app.run(debug=True)
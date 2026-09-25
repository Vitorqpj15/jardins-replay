import cv2
import time
import sqlite3
from datetime import datetime
from collections import deque

SEGUNDOS_ANTES = 10
SEGUNDOS_DEPOIS = 3

conn = sqlite3.connect("pelada.db")
cursor = conn.cursor()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Não foi possível acessar a câmera.")
    exit()

fps_real = cap.get(cv2.CAP_PROP_FPS)
if fps_real <= 0:
    fps_real = 20
    print("Câmera não informou FPS válido, usando valor padrão de 20.")

largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"FPS da câmera: {fps_real} | Resolução: {largura}x{altura}")

tamanho_buffer = int(fps_real * SEGUNDOS_ANTES)
buffer = deque(maxlen=tamanho_buffer)

gravando_lance = False
frames_extra_restantes = 0
frames_do_lance = []

while True:
    ret, frame = cap.read()

    if not ret:
        print("Falha ao capturar o frame.")
        break

    buffer.append(frame)
    cv2.imshow("Pelada Replay - aperte ESPAÇO para salvar um lance", frame)

    tecla = cv2.waitKey(1) & 0xFF

    if tecla == ord(' ') and not gravando_lance:
        print("Lance marcado! Capturando os segundos seguintes...")
        gravando_lance = True
        frames_do_lance = list(buffer)
        frames_extra_restantes = int(fps_real * SEGUNDOS_DEPOIS)

    if gravando_lance:
        frames_do_lance.append(frame)
        frames_extra_restantes -= 1

        if frames_extra_restantes <= 0:
            nome_arquivo = f"lances/lance_{int(time.time())}.mp4"
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            writer = cv2.VideoWriter(nome_arquivo, fourcc, fps_real, (largura, altura))

            for f in frames_do_lance:
                writer.write(f)

            writer.release()
            print(f"Lance salvo em: {nome_arquivo}")

            
            data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(
                "INSERT INTO lances (nome_arquivo, data_hora) VALUES (?, ?)",
                (nome_arquivo, data_hora_atual)
            )
            conn.commit()
            print("Lance registrado no banco de dados.")

            gravando_lance = False
            frames_do_lance = []

    if tecla == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
conn.close()
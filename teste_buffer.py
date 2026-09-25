import cv2
from collections import deque

SEGUNDOS_DE_BUFFER = 5

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Não foi possível acessar a câmera.")
    exit()

fps_real = cap.get(cv2.CAP_PROP_FPS)

if fps_real <= 0:
    fps_real = 20  
    print("Câmera não informou FPS válido, usando valor padrão de 20.")

print(f"FPS da câmera: {fps_real}")

TAMANHO_BUFFER = int(fps_real * SEGUNDOS_DE_BUFFER)
buffer = deque(maxlen=TAMANHO_BUFFER)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Falha ao capturar o frame.")
        break

    buffer.append(frame)

    cv2.imshow("Teste de buffer", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Frames no buffer ao encerrar: {len(buffer)}")
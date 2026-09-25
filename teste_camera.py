import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Não foi possível acessar a câmera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Falha ao capturar o frame.")
        break

    cv2.imshow("Teste de câmera", frame)

    # Encerra o loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
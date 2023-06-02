import cv2

# Ruta del archivo de video de entrada
input_file = 'video.mp4'

# Crear objeto de captura de video
cap = cv2.VideoCapture(input_file)

# Verificar si se abrió correctamente el archivo de video
if not cap.isOpened():
    print("Error al abrir el archivo de video.")

else:
    # Procesa el video aquí
    pass

cap.release()

# Obtener información del video
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Mostrar información del video
print(f"FPS: {fps}")
print(f"Ancho: {width}")
print(f"Alto: {height}")
print(f"Total de fotogramas: {frame_count}")

# Iterar sobre los fotogramas del video
while True:
    # Leer el siguiente fotograma
    ret, frame = cap.read()

    # Verificar si se llegó al final del video
    if not ret:
        break

    # Procesar el fotograma aquí
    # ...

    # Mostrar el fotograma procesado
    cv2.imshow('Video', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()


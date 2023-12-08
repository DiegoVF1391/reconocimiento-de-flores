import cv2 as cv

# Ruta del archivo de video
video_path = 'D:/Descargas/flores/tu.MOV'  # Reemplaza esto con la ruta correcta de tu video

Cap = cv.VideoCapture(video_path)
i = 4464

while True:
    ret, frame = Cap.read()

    if not ret:
        break

    #color = (0,0,255)
    #esquinaSuperior = (10, 10)
    #esquinaInferior = (470, 470)
    florChica = cv.resize(frame, (26, 26))
    cv.imwrite('C:/Users/Diego/Desktop/IA/reconocimiento_flores/flores/tulipan/tulipan' + str(i) + '.jpg', florChica)
    i += 1

print('Terminado')
Cap.release()
cv.destroyAllWindows()
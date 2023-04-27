import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# crear objeto de captura de la webcam
cap = cv2.VideoCapture(0)

# crear objeto para la deteccion
detector = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

while cap.isOpened():
    # capturar la imagen
    success, img = cap.read()
    if not success:
        print("empty frame")
        continue

    # procesar imagen
    # Cambiar espacio de color de BGR (opencv) a RGB (mediapipe)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    prediction = detector.process(img)

    # convertir a BGR de nuevo
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # dibujar resultados en la imagen
    if prediction.detections:
        for detection in prediction.detections:
            mp_drawing.draw_detection(img, detection)

    # desplegar la imagen
    cv2.imshow("mediapipe face detection", img)

    if cv2.waitKey(5) & 0XFF == 27:
        break

cap.release()

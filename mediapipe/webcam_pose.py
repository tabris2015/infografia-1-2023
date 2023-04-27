import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
# drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# crear objeto de captura de la webcam
cap = cv2.VideoCapture(0)

# crear objeto para la deteccion
detector = mp.solutions.pose.Pose(
    model_complexity=2
    )

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
    if prediction.pose_landmarks.landmark[0]:
        print(f"Rostro: {prediction.pose_landmarks.landmark[0]}")
    # dibujar resultados en la imagen
    if prediction.pose_landmarks:
        mp_drawing.draw_landmarks(
            img,
            prediction.pose_landmarks,
            mp.solutions.pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
        )

    # desplegar la imagen
    cv2.imshow("mediapipe pose detection", img)

    if cv2.waitKey(5) & 0XFF == 27:
        break

cap.release()

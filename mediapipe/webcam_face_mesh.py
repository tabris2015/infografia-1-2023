import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# crear objeto de captura de la webcam
cap = cv2.VideoCapture(0)

# crear objeto para la deteccion
detector = mp.solutions.face_mesh.FaceMesh(
    max_num_faces=2,
    refine_landmarks=True
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

    # dibujar resultados en la imagen
    for face_landmarks in prediction.multi_face_landmarks:
        # print(face_landmarks)
        mp_drawing.draw_landmarks(
            image=img,
            landmark_list=face_landmarks,
            connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
        )

    # desplegar la imagen
    cv2.imshow("mediapipe face detection", img)

    if cv2.waitKey(5) & 0XFF == 27:
        break

cap.release()

import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

BG_COLOR = (70, 70, 70)
cap = cv2.VideoCapture(0)

with mp_selfie_segmentation.SelfieSegmentation(
    model_selection=1) as selfie_segmentation:

    bg_image = None
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = selfie_segmentation.process(image)
        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        condition = np.stack((results.segmentation_mask, ) * 3, axis=-1) > 0.1
        print(condition.shape, image.shape, f"-> {condition[0, 0]}")

        if bg_image is None:
            bg_image = np.zeros(image.shape, dtype=np.uint8)
            bg_image[:] = BG_COLOR
        output_image = np.where(condition, bg_image, image)

        cv2.imshow("selfie", output_image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
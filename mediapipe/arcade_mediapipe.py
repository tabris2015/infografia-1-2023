import arcade
import mediapipe as mp
import cv2

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Deteccion de pose y arcade"


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.cap = cv2.VideoCapture(0)
        self.detector = mp.solutions.pose.Pose()
        self.img = None
        self.prediction = None

    def on_update(self, delta_time: float):
        """Metodo para actualizar objetos de la app"""
        if self.cap.isOpened():
            success, self.img = self.cap.read()
            if success:
                self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                self.prediction = self.detector.process(self.img)

    def on_draw(self):
        """Metodo para dibujar en la pantalla"""
        arcade.start_render()
        self.draw_pose()
        
    
    def draw_pose(self):
        # dibujar un circulo solamente en la nariz
        landmarks = self.prediction.pose_landmarks.landmark
        interesting_landmarks = [landmarks[0]]
        interesting_landmarks.append(landmarks[2])
        interesting_landmarks.append(landmarks[5])
        interesting_landmarks = interesting_landmarks + landmarks[11:23]
        
        for l in interesting_landmarks:
            if l is not None:
                l_x, l_y = l.x, l.y
                pixel_x = l_x * SCREEN_WIDTH
                pixel_y = SCREEN_HEIGHT - l_y * SCREEN_HEIGHT
                arcade.draw_circle_outline(
                    pixel_x,
                    pixel_y,
                    10,
                    arcade.color.RED
                )
                print(f"{(pixel_x, pixel_y)}")



if __name__ == "__main__":
    app = App()
    arcade.run()

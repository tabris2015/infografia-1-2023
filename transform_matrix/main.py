import arcade
import numpy as np
from polygon import Polygon

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "matrices de transformacion"


class TransformWindow(arcade.Window):
    def __init__(self, polygon: Polygon):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.polygon = polygon

    def on_draw(self):
        arcade.start_render()
        self.polygon.draw()
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            Tr = np.array([
                [1, 0, 0], 
                [0, 1, 5], 
                [0, 0, 1]
            ])
            self.polygon.transform(Tr)
            # self.polygon.move(0, 5)
    

def main():
    poly = Polygon([(40, 40), (200, 40), (120, 300)])
    app = TransformWindow(poly)
    arcade.run()


if __name__ == "__main__":
    main()

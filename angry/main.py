import math

import arcade
import pymunk

from game_object import Bird, Column

WIDTH = 800
HEIGHT = 800
TITLE = "Angry birds"


class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        # crear espacio de pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)

        # agregar piso
        floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape = pymunk.Segment(floor_body, [0, 50], [WIDTH, 50], 0.0)
        floor_shape.friction = 10
        self.space.add(floor_body, floor_shape)

        self.bird = Bird("assets/img/red-bird3.png", 0, 0, WIDTH / 2, HEIGHT / 2, self.space)

        self.sprites = arcade.SpriteList()
        self.sprites.append(self.bird)
        self.add_columns()

    def add_columns(self):
        for x in range(WIDTH // 2, WIDTH, 50):
            column = Column("assets/img/column.png", x, 100, self.space)
            self.sprites.append(column)

    def on_update(self, delta_time: float):
        self.space.step(1 / 60.0)   # actualiza la simulacion de las fisicas
        self.sprites.update()

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            bird = Bird("assets/img/red-bird3.png", 50, math.radians(45), x, y, self.space)
            self.sprites.append(bird)


def main():
    app = App()
    arcade.run()


if __name__ == "__main__":
    main()
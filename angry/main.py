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

        self.sprites = arcade.SpriteList()
        self.add_columns()

        self.start_point = ()
        self.end_point = ()
        self.distance = 0
        self.draw_line = False

    def add_columns(self):
        for x in range(WIDTH // 2, WIDTH, 50):
            column = Column("assets/img/column.png", x, 100, self.space)
            self.sprites.append(column)

    def on_update(self, delta_time: float):
        self.space.step(1 / 60.0)   # actualiza la simulacion de las fisicas
        self.sprites.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("clic")
            self.start_point = (x, y)
            self.end_point = (x, y)
            self.draw_line = True

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if buttons == arcade.MOUSE_BUTTON_LEFT:
            self.end_point = (x, y)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("release")
            self.draw_line = False
            angle = -arcade.get_angle_radians(
                self.start_point[0],
                self.start_point[1],
                self.end_point[0],
                self.end_point[1],
            ) - math.pi / 2
            self.distance = arcade.get_distance(
                self.start_point[0],
                self.start_point[1],
                self.end_point[0],
                self.end_point[1],
            )
            print(angle, self.distance)
            bird = Bird("assets/img/red-bird3.png", self.distance, angle, x, y, self.space)
            self.sprites.append(bird)

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()
        if self.draw_line:
            arcade.draw_line(self.start_point[0], self.start_point[1], self.end_point[0], self.end_point[1], arcade.color.BLACK, 3)


def main():
    app = App()
    arcade.run()


if __name__ == "__main__":
    main()
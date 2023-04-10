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
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_color = arcade.color.GREEN
        self.draw_line_to_center = False
        self.rotation_angle = 0

    def on_draw(self):
        arcade.start_render()
        self.polygon.draw()
        arcade.draw_circle_filled(self.mouse_x, self.mouse_y, 20, self.mouse_color)
        if self.draw_line_to_center:
            arcade.draw_line(self.polygon.x, self.polygon.y, self.mouse_x, self.mouse_y, arcade.color.RED)
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.polygon.translate(0, 5)
        if symbol == arcade.key.DOWN:
            self.polygon.translate(0, -5)
        if symbol == arcade.key.LEFT:
            self.polygon.translate(-5, 0)
        if symbol == arcade.key.RIGHT:
            self.polygon.translate(5, 0)
        if symbol == arcade.key.E:
            self.polygon.rotate(5)
        if symbol == arcade.key.Q:
            self.polygon.rotate(-5)
        if symbol == arcade.key.Y:
            self.polygon.scale(1.2, 1.2)
        if symbol == arcade.key.H:
            self.polygon.scale(0.9, 0.9)

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if buttons == arcade.MOUSE_BUTTON_LEFT and arcade.is_point_in_polygon(x, y, self.polygon.vertices):
            self.mouse_x = x
            self.mouse_y = y
            self.mouse_color = arcade.color.GREEN
            self.polygon.translate(dx, dy)
        if buttons == arcade.MOUSE_BUTTON_RIGHT:
            self.mouse_x = x
            self.mouse_y = y
            self.mouse_color = arcade.color.RED
            self.draw_line_to_center = True
            target_angle = -arcade.get_angle_degrees(self.polygon.x, self.polygon.y, x, y) + 90
            self.rotation_angle = target_angle - self.polygon.theta
            print(self.polygon.theta, self.rotation_angle, target_angle)
            self.polygon.rotate(self.rotation_angle)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.draw_line_to_center = False

        


def main():
    poly = Polygon([(40, 40), (200, 40), (120, 300)])
    app = TransformWindow(poly)
    arcade.run()


if __name__ == "__main__":
    main()

import math

import arcade
import pymunk


WIDTH = 800
HEIGHT = 800
TITLE = "Hello pymunk"


class Mario(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y, shape):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.shape = shape


class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)
        # crear espacio de pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)

        # agregar piso
        floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape = pymunk.Segment(floor_body, [0, 50], [WIDTH, 50], 0.0)
        floor_shape.friction = 10
        self.space.add(floor_body, floor_shape)

        body = pymunk.Body(1.0, pymunk.moment_for_box(1.0, (30, 30)))
        body.position = pymunk.Vec2d(WIDTH / 2, HEIGHT / 2)
        shape = pymunk.Poly.create_box(body, (30, 30))
        shape.elasticity = 0.2
        shape.friction = 0.8
        # agregar shape al espacio
        self.space.add(body, shape)

        self.mario = Mario("img/mario.png", 0.3, WIDTH / 2, HEIGHT / 2, shape)

        self.sprites = arcade.SpriteList()
        self.sprites.append(self.mario)

    def on_update(self, delta_time: float):
        self.space.step(1 / 60.0)   # actualiza la simulacion de las fisicas
        for sprite in self.sprites:
            sprite.center_x = sprite.shape.body.position.x
            sprite.center_y = sprite.shape.body.position.y
            sprite.angle = math.degrees(sprite.shape.body.angle)

        self.sprites.update()

    def on_draw(self):
        arcade.start_render()
        self.clear()
        self.sprites.draw()


def main():
    app = App()
    arcade.run()


if __name__ == "__main__":
    main()
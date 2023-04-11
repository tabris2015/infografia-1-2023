import math

import arcade
import pymunk


class Bird(arcade.Sprite):
    def __init__(self, image: str, distance: float, angle: float, x: float, y: float, space: pymunk.Space):
        super().__init__(image, 1)
        self.health = 20
        mass = 5
        radius = 12
        moment = pymunk.moment_for_circle(mass, 0, radius)
        body = pymunk.Body(mass, moment)
        body.position = (x, y)
        power = distance * 50
        impulse = power * pymunk.Vec2d(1, 0)
        body.apply_impulse_at_local_point(impulse.rotated(angle))
        shape = pymunk.Circle(body, radius)
        shape.elasticity = 0.8
        shape.friction = 1

        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def update(self):
        self.center_x = self.shape.body.position.x
        self.center_y = self.shape.body.position.y
        self.angle = math.degrees(self.shape.body.angle)


class Column(arcade.Sprite):
    def __init__(self, image: str, x: float, y: float, space: pymunk.Space):
        super().__init__(image, 1)
        mass = 2
        moment = pymunk.moment_for_box(mass, (self.width, self.height))
        body = pymunk.Body(mass, moment)
        body.position = (x, y)
        shape = pymunk.Poly.create_box(body, (self.width, self.height))
        shape.elasticity = 0.8
        shape.friction = 0.4
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def update(self):
        self.center_x = self.shape.body.position.x
        self.center_y = self.shape.body.position.y
        self.angle = math.degrees(self.shape.body.angle)

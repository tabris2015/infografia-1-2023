import arcade

class Polygon:
    def __init__(self, vertices, color=arcade.color.RED):
        self.vertices = vertices # [(x, y), ...]
        self.color = color
        self.line_width = 4

    def draw(self):
        arcade.draw_polygon_outline(
            self.vertices,
            self.color,
            4
        )
    
    def move(self, dx: int, dy:int):
        for i, v in enumerate(self.vertices):
            self.vertices[i] = (v[0] + dx, v[1] + dy)
    
    
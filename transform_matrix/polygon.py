import arcade
import numpy as np

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

    def transform(self, t_matrix):
        # 1. Convertir vertices a una matrix de (3, n)
        vert_list = [[v[0], v[1], 1] for v in self.vertices]
        vert_matrix = np.transpose(np.array(vert_list))
        # 2. Aplicar la matriz de transformacion
        new_matrix = np.dot(t_matrix, vert_matrix)
        # 3. Convertir nuevos vertices al formato [(x, y), ...]
        new_matrix2 = np.transpose(new_matrix)
        new_vertices = [(nv[0], nv[1]) for nv in new_matrix2]
        # 4. Reasignar nuevos vertices
        self.vertices = new_vertices
    


if __name__ == "__main__":
    p = Polygon([(40, 40), (200, 40), (120, 300)])
    Tr = np.array([
        [1, 0, 100], 
        [0, 1, 100], 
        [0, 0, 1]
    ])
    p.transform(Tr)
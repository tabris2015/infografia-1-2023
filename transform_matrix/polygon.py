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

    def translate(self, dx, dy):
        trf = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ])
        self.transform(trf)
    
    def rotate(self, theta):
        vert_array = np.array(self.vertices)
        center = np.sum(vert_array, axis=0) / vert_array.shape[0]
        # M1
        to_origin_trf = np.array([
            [1, 0, -center[0]],
            [0, 1, -center[1]],
            [0, 0, 1]
        ])
        # M2
        rotation_trf = np.array([
            [np.cos(np.radians(theta)), -np.sin(np.radians(theta)), 0],
            [np.sin(np.radians(theta)), np.cos(np.radians(theta)), 0],
            [0, 0, 1]
        ])
        # M3
        from_origin_trf = np.array([
            [1, 0, center[0]],
            [0, 1, center[1]],
            [0, 0, 1]
        ])
        #                          <------------------------<---------------<-----                                             
        #                          M3                       M2              M1
        self.transform(np.dot(from_origin_trf, np.dot(rotation_trf, to_origin_trf)))
    
    def scale(self, sx, sy):
        trf = np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ])
        self.transform(trf)
    


if __name__ == "__main__":
    p = Polygon([(40, 40), (200, 40), (120, 300)])
    p.rotate(5)
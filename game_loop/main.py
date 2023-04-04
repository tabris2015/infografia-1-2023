import arcade

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Lineas con bresenham"


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.px = SCREEN_WIDTH / 2
        self.py = SCREEN_HEIGHT / 2 # comienza en el centro de la pantalla
        self.movement = 5
        self.points = []

    def on_key_press(self, symbol: int, modifiers: int):
        """Metodo para detectar teclas que han sido presionada
        El punto se movera con las teclas de direccion.
        Argumentos:
            symbol: tecla presionada
            modifiers: modificadores presionados
        """
        if symbol == arcade.key.UP:
            print("arriba")
            self.py += self.movement
        if symbol == arcade.key.DOWN:
            print("abajo")
            self.py -= self.movement
        if symbol == arcade.key.LEFT:
            print("izquierda")
            self.px -= self.movement
        if symbol == arcade.key.RIGHT:
            print("derecha")
            self.px += self.movement

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """Metodo para detectar clics del mouse
        En la posicion del clic, se agregara un nuevo punto
        Argumentos:
            x: coordenada x del clic
            y: coordenada y del clic
            button: boton del mouse presionado
            modifiers: teclas modificadoras presionadas (shift, ctrl, etc)
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(f"Agregando punto ({x}, {y})")
            self.points.append((x, y))

    def on_update(self, delta_time: float):
        """Metodo para actualizar objetos de la app"""
        colision = self.player_is_on_food()
        if colision != -1:
            print(f"Colision con el punto {colision}: {self.points[colision]}")

    def player_is_on_food(self):
        """Funcion que detecta si el jugador ha colisionado
        con un punto.
        Devuelve el indice del punto en la lista self.points si 
        existe una colision.
        Si no existe la colision, devuelve el valor de -1.
        Ejemplo:
        self.points = [
        0:    (3, 4),
        1:    (6, 7),
        2:    (18, 20)
            ]
        jugador colisiona con punto en (6, 7): retornar 1
        jugador no colisiona con ningun punto: retornar -1
        """
        return -1

    def on_draw(self):
        """Metodo para dibujar en la pantalla"""
        arcade.start_render()
        arcade.draw_point(self.px, self.py, arcade.color.RED, 10)
        if self.points:
            arcade.draw_points(self.points, arcade.color.GREEN, 5)


if __name__ == "__main__":
    app = App()
    arcade.run()

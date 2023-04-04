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
        """Metodo para detectar clics del mouse"""

    def on_update(self, delta_time: float):
        """Metodo para actualizar objetos de la app"""

    def on_draw(self):
        """Metodo para dibujar en la pantalla"""
        arcade.start_render()
        arcade.draw_point(self.px, self.py, arcade.color.RED, 5)


if __name__ == "__main__":
    app = App()
    arcade.run()

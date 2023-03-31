import arcade
from hello_arcade import draw_flower

# definicion de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"

# Definicion de clase ventana
class Hola(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        # iniciar renderizado
        arcade.start_render()

        # dibujar
        draw_flower()


# entrypoint
if __name__ == "__main__":
    app = Hola()
    arcade.run()
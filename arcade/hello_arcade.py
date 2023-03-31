# importamos el paquete
import arcade
import math
import cmath

# definicion de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"

def draw_flower():
    petal_number = 16
    final_angle = 360
    angle_step = final_angle // petal_number
    
    for angle in range(0, final_angle, angle_step):
        r = 70 + int(angle / 3)
        phi = math.radians(angle)
        center_c = cmath.rect(r, phi)
        arcade.draw_circle_filled(
            int(center_c.real + SCREEN_WIDTH / 2),
            int(center_c.imag + SCREEN_HEIGHT / 2),
            30,
            arcade.color.RED_ORANGE
        )

    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50, arcade.color.YELLOW)


if __name__ == "__main__":
    # Crear nueva ventana
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Cambiar el color de fondo
    arcade.set_background_color(arcade.color.WHITE)

    # iniciar render
    arcade.start_render()

    # Funciones para dibujar
    draw_flower()

    # finalizar render
    arcade.finish_render()

    # Correr el programa
    arcade.run()

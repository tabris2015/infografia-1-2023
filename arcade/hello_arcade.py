# importamos el paquete
import arcade

# definicion de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"

# Crear nueva ventana
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Cambiar el color de fondo
arcade.set_background_color(arcade.color.WHITE)

# iniciar render
arcade.start_render()

# Funciones para dibujar
arcade.draw_circle_filled(
    SCREEN_WIDTH / 2, 
    SCREEN_HEIGHT / 2, 
    100, 
    arcade.color.CYBER_GRAPE
    )

arcade.draw_lrtb_rectangle_filled(
    50,
    150,
    150,
    50,
    arcade.color.AFRICAN_VIOLET
)

# finalizar render
arcade.finish_render()

# Correr el programa
arcade.run()

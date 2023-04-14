extends KinematicBody2D

# variable disponible en el inspector
export (int) var speed = 100

var target
var velocity = Vector2()

func _ready():
	target = position

func _input(event):
	if event.is_action_pressed("click"):
		target = get_global_mouse_position()
		print(target)

func _physics_process(delta):
	# calcular el vector de velocidad
	velocity = position.direction_to(target) * speed
	
	# si esta lejos del target, se mueve en esa direccion
	if position.distance_to(target) > 5:
		velocity = move_and_slide(velocity)

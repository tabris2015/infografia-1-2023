extends KinematicBody2D


onready var state_machine = $AnimationTree.get("parameters/playback")
onready var start_position = global_position
onready var target_position = global_position
onready var timer = $Timer

export(int) var move_range = 500

var speed = 60
var accel = 130
var velocity = Vector2.ZERO

# se invoca en cada frame
func _physics_process(delta):
	# calcular la direccion a donde moverse
	var direction = global_position.direction_to(target_position).normalized()
	
	if direction.x < 0:
		$Sprite.scale.x = -1
	elif direction.x > 0:
		$Sprite.scale.x = 1
	
	# calcular la velocidad 
	if global_position.distance_to(target_position) > 20:
		velocity = velocity.move_toward(direction * speed, accel * delta)
	else:
		# si es que ya estoy cerca de la position objetivo
		velocity = velocity.move_toward(Vector2.ZERO, accel * delta)
		
	if velocity.length() < 1:
		state_machine.travel("enemy_idle")
	# mover con velocidad
	move_and_slide(velocity)
	
#func _input(event):
#	if event.is_action_pressed("click"):
#		target_position = get_global_mouse_position()
#		print(global_position.distance_to(target_position))
		

func _on_Timer_timeout():
	#print("patrullar!")
	# calcular una nueva posicion aleatoria dentro del rango para moverse
	target_position = Vector2(rand_range(0, move_range), rand_range(0, move_range))
	state_machine.travel("enemy_walk")
	# definir una duracion aleatoria entre 10 y 20 segundos
	var duration = rand_range(10, 20)
	#print("esperando ", duration, " segundos")
	# iniciar el timer con esa duracion
	timer.start(duration)

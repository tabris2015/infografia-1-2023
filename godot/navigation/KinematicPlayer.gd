extends KinematicBody2D

signal compute_path(start_position, target_position)

export var speed = 60
export var accel = 130
var velocity = Vector2.ZERO
var path = PoolVector2Array()
var next_position = 0

func _input(event):
	if event.is_action_pressed("click"):
		# informar al main que calcule el camino
		emit_signal("compute_path", global_position, get_global_mouse_position())

func _physics_process(delta):
	var target_position = Vector2.ZERO
	if len(path) > 0:
		target_position = path[next_position]
		#print("next: ", target_position)
	else:
		target_position = global_position
		
	var direction = global_position.direction_to(target_position).normalized()
	
	if global_position.distance_to(target_position) > 20:
		velocity = velocity.move_toward(direction * speed, accel * delta)
	else:
		# si es que ya estoy cerca de la position objetivo
		velocity = velocity.move_toward(Vector2.ZERO, accel * delta)
		
	if velocity.length() < 1:
		next_position += 1
		if next_position >= len(path) - 1:
			next_position = len(path) - 1
		#print("incrementando siguiente posicion")
		
	# mover con velocidad
	move_and_slide(velocity)


func _on_Main_send_path(new_path):
	print("received path:", new_path)
	path = new_path
	next_position = 0



func _on_Map_send_path(new_path):
	print("received path:", new_path)
	path = new_path
	next_position = 0


func _on_Map2_send_path(new_path):
	print("received path:", new_path)
	path = new_path
	next_position = 0

extends Sprite

signal compute_path(start_position, target_position)

export var speed = 80
var path = PoolVector2Array()

func _input(event):
	if event.is_action_pressed("click"):
		# informar al main que calcule el camino
		emit_signal("compute_path", global_position, get_global_mouse_position())

func _on_Main_send_path(path):
	print("received path: ", path)

extends Node2D

signal send_path(path)

var path = PoolVector2Array()


func _on_KinematicPlayer_compute_path(start_position, target_position):
	path = $Navigation2D.get_simple_path(start_position, target_position)
	emit_signal("send_path", path)
	#dibujar la ruta
	$Line2D.points = path

extends RigidBody2D

var impulse = false

func _unhandled_input(event):
	if event.is_action_pressed("ui_right"):
		impulse = true

func _physics_process(delta):
	
	if impulse:
		apply_impulse(Vector2.ZERO, Vector2(150, -150))
		impulse = false

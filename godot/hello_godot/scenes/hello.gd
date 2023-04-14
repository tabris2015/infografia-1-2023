extends Node2D

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Polling
	if(Input.is_key_pressed(KEY_LEFT)):
		self.position.x -= 1
	if(Input.is_key_pressed(KEY_RIGHT)):
		self.position.x += 1
	if(Input.is_key_pressed(KEY_DOWN)):
		self.position.y -= 1
	if(Input.is_key_pressed(KEY_UP)):
		self.position.y += 1

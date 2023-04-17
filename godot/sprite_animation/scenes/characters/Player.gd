extends KinematicBody2D

var is_atacking = false
var anim_state = "IDLE"

func _input(event):
	if event.is_action_pressed("attack"):
		print("atacar!")
		anim_state = "ATTACK"
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if anim_state == "ATTACK":
		$AnimationPlayer.play("player_attack")
		anim_state = "IDLE"
		print("atando")
		
	elif anim_state == "IDLE" and not $AnimationPlayer.is_playing():
		$AnimationPlayer.play("player_idle")

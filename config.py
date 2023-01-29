#GLOBAL VARIABLES
from images import *
import os 

#initialization method
def intitialize():
	global game_state
	global switch
	global stage
	global volume
	global start_rect
	global control_rect
	global lifes
	global score
	global last_score
	global high_score
	global moving_right
	global moving_left
	global asteroid_vel
	global asteroid_list
	global asteroid_num
	global y_max
	global y_min
	global link_color
	global current_rocket
	global powers_count
	global powers
	global power_list
	global power_ups
	global spawned

	# - - - - high_score_storage - - - - #
	if os.path.exists('high_score.txt'):
		with open('high_score.txt', 'r') as file:
			high_score = int(file.read())

	else:
		high_score = 0
	# - - - - - - - - - - - - - - - - - #
	spawned = False
	powers_count = 0
	powers = [wipeout,rocket]
	power_ups = []
	power_list = []
	link_color = (255,255,255)
	y_max = -2500
	y_min = -200
	asteroid_num = 10
	asteroid_list = []
	asteroid_vel = 2
	moving_left = False
	moving_right = False 
	last_score = None
	game_state = True
	current_rocket = 0
	score = 0
	lifes = 3
	switch = 1
	stage = 0
	volume = 0.2
	start_rect = start_button.get_rect(center = [640,400])
	control_rect = control_button.get_rect(center = [640,600]) 

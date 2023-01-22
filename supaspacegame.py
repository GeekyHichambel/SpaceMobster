#MAIN_GAME
import pygame as pg
import sys
from GAME_FUNC import scene
import config
import music
import images as ig
#screen_setup
screen_width = 1280
screen_height = 720
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption('Space Mobster')
#initializations
pg.init()
config.intitialize()
music.volume_set()
music.load()
ig.perf()
#game_loop
while config.game_state:

	if config.switch == 1:
		scene.main_menu(screen)

	elif config.switch == 2:
		scene.control_menu(screen)

	elif config.switch == 3:
		scene.main_game(screen)

	elif config.switch == 4:
		scene.game_over(screen)

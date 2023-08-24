#Music Library
import pygame as pg
import os
from pygame import mixer
import config

pg.mixer.pre_init(44100, -16, 2, 512)
pg.init()
pg.mixer.init()
#music resources
switch_sfx = pg.mixer.Sound(os.path.join("resources","switch__.wav"))
selector_sfx = pg.mixer.Sound(os.path.join("resources","selector.mp3"))
life_lost_sfx = pg.mixer.Sound(os.path.join("resources","life_lost.wav"))
game_over_sfx = pg.mixer.Sound(os.path.join("resources","game_over.wav"))
life_gain_sfx = pg.mixer.Sound(os.path.join("resources","lifegain.wav"))
wipeout_sfx = pg.mixer.Sound(os.path.join("resources","wipeout.wav"))
#functions
def load():
	mixer.music.load(os.path.join("resources","CYBERPUNK.mp3"))
	mixer.music.play(-1)

def unload():
	mixer.music.unload()

def volume_set():
	mixer.music.set_volume(config.volume)
	switch_sfx.set_volume(config.volume)
	selector_sfx.set_volume(config.volume)
	life_lost_sfx.set_volume(config.volume)
	life_gain_sfx.set_volume(config.volume) 
	game_over_sfx.set_volume(config.volume)
	wipeout_sfx.set_volume(config.volume)

def volume_mute():
	if config.volume > 0.0:
		config.volume = 0.0
		print('muted')
		volume_set()

	else:
		config.volume = 0.2
		print('unmuted')
		volume_set()

def volume_plus():
	if config.volume == 1.0:
		print('max')

	else:
		config.volume+=(0.1)
		config.volume = round(config.volume,1)
		print(config.volume)
		volume_set()

def volume_minus():
	if config.volume == 0.0:
		print('min')

	else:
		config.volume-=(0.1)
		config.volume = round(config.volume,1)
		print(config.volume)
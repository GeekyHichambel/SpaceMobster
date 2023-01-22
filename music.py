#Music Library
import pygame as pg
import os
from pygame import mixer
import config

pg.init()
#music resources
switch_sfx = pg.mixer.Sound(os.path.join("resources","switch__.wav"))
selector_sfx = pg.mixer.Sound(os.path.join("resources","selector.mp3"))
life_lost_sfx = pg.mixer.Sound(os.path.join("resources","life_lost.wav"))
game_over_sfx = pg.mixer.Sound(os.path.join("resources","game_over.wav"))
#music functions
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
	game_over_sfx.set_volume(config.volume)

def volume_mute():
	if config.volume > 0.0:
		config.volume = 0.0
		print('muted')
		mixer.music.set_volume(config.volume)
		switch_sfx.set_volume(config.volume)
		selector_sfx.set_volume(config.volume)
		life_lost_sfx.set_volume(config.volume)
		game_over_sfx.set_volume(config.volume)

	else:
		config.volume = 0.2
		print('unmuted')
		mixer.music.set_volume(config.volume)
		switch_sfx.set_volume(config.volume)
		selector_sfx.set_volume(config.volume)
		life_lost_sfx.set_volume(config.volume)
		game_over_sfx.set_volume(config.volume)

def volume_plus():
	if config.volume == 1.0:
		print('max')

	else:
		config.volume+=(0.1)
		config.volume = round(config.volume,1)
		print(config.volume)
		mixer.music.set_volume(config.volume)
		switch_sfx.set_volume(config.volume)
		selector_sfx.set_volume(config.volume)
		life_lost_sfx.set_volume(config.volume)
		game_over_sfx.set_volume(config.volume)

def volume_minus():
	if config.volume == 0.0:
		print('min')

	else:
		config.volume-=(0.1)
		config.volume = round(config.volume,1)
		print(config.volume)
		mixer.music.set_volume(config.volume)
		switch_sfx.set_volume(config.volume)
		selector_sfx.set_volume(config.volume)
		life_lost_sfx.set_volume(config.volume)
		game_over_sfx.set_volume(config.volume)

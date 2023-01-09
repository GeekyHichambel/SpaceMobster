#Game functions
import pygame as pg
import os
import random
import sys
import images as ig
import music
from music import *
import config
import webbrowser
from rocket import lifes
from rocket import res
from rocket import ship
#initializations
pg.font.init()
fps = pg.time.Clock()
frames = 60
window = 1
#text
game_font = pg.font.SysFont("bahnschrift", 50 , bold = True)
small_game_font = pg.font.SysFont("comic sans", 25 , bold = True)
super_small_game_font = pg.font.SysFont("comic sans", 20, bold = True)
class SCENE():
	def __init__(self):
		pass

# - - - - - MAIN-GAME - - - - - #
	def main_menu(self,screen):
		global window
		fps.tick(frames)
		screen.blit(ig.main_menu,(0,0))
		screen.blit(ig.current_start,config.start_rect)
		screen.blit(ig.current_control,config.control_rect)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				config.game_state = False

			if event.type == pg.KEYDOWN:

				if event.key == pg.K_ESCAPE:
					config.game_state = False

				if event.key == pg.K_RETURN:
					if window == 2:
						switch_sfx.play()
						config.switch = window
						break

					elif window == 3:
						switch_sfx.play()
						config.switch = window
						break

				if event.key == pg.K_UP:
					selector_sfx.play()
					ig.current_start = ig.start_button_2
					ig.current_control = ig.control_button
					window = 3

				elif event.key == pg.K_DOWN:
					selector_sfx.play()
					ig.current_control = ig.control_button_2
					ig.current_start = ig.start_button
					window = 2

				if event.key == pg.K_m:
					music.volume_mute()

				if event.key == pg.K_KP_PLUS:
					music.volume_plus()

				if event.key == pg.K_KP_MINUS:
					music.volume_minus() 

		pg.display.update()
			
# - - - - - - - CONTROLS - - - - - - #
	def control_menu(self,screen):
		global window
		screen.fill('black')
		screen.blit(ig.control_screen,(0,0))
		fps.tick(frames)

		high_score_text = small_game_font.render(f"HIGH SCORE: {config.high_score}", 1,(255,255,255))
		creator = small_game_font.render("Made with love by:", 1, (255,255,255))
		creator_link = screen.blit(super_small_game_font.render("https://github.com/GeekyHichambel", 1, config.link_color),(880,600))

		for event in pg.event.get():
			if event.type == pg.QUIT:
				config.game_state = False

			if event.type == pg.KEYDOWN:

				if event.key == pg.K_ESCAPE:
					switch_sfx.play()
					config.switch = 1

				if event.key == pg.K_m:
					music.volume_mute()

				if event.key == pg.K_KP_PLUS:
					music.volume_plus()

				if event.key == pg.K_KP_MINUS:
					music.volume_minus()

			if event.type == pg.MOUSEBUTTONDOWN:
				pos = event.pos

				if creator_link.collidepoint(pos):
					webbrowser.open(r"https://github.com/GeekyHichambel")
			
		if creator_link.collidepoint(pg.mouse.get_pos()):
			config.link_color = (77,255,77)
		else:
			config.link_color = (255,255,255)

		screen.blit(high_score_text,(880,380))
		screen.blit(creator,(880,490))
		pg.display.update()

# - - - - - - - - MAIN-GAME - - - - - - #
	def main_game(self,screen):
		global window
		if len(config.Asteroids) == 0:
			config.stage += 1
			config.asteroid_vel = round(config.asteroid_vel+0.8,1) 
			print('SHOWER SPEED :'+str(config.asteroid_vel))
			if config.asteroid_num + config.stage >= 20:
				config.asteroid_num = 20
			else:
				config.asteroid_num += config.stage
			for i in range(config.asteroid_num):
				asteroid = Asteroid(random.randrange(0,1180), random.randrange(config.y_max,config.y_min)) 
				config.Asteroids.append(asteroid)
				asteroid_grp.add(asteroid)

		config.start_time = pg.time.get_ticks()
		config.score += round(config.start_time/1000)

		screen.fill('black')
		fps.tick(frames)
		stage_text = game_font.render(f"STAGE: {config.stage}", 1, (102,0,102))
		score_text = game_font.render(f"SCORE: {config.score}", 1, (102,0,102))

		for event in pg.event.get():
			if event.type == pg.QUIT:
				config.game_state = False

			if event.type == pg.KEYDOWN:

				if event.key == pg.K_ESCAPE:
					switch_sfx.play()
					res.reset()
					res.restart()

				if event.key == pg.K_SPACE:
					if config.lifes == 0:
						config.switch = 4
						config.last_score = config.score
						config.score = 0
						config.start_time = 0 
						game_over_sfx.play()
						break

					else:
						config.lifes -= 1
						lifes.pop(config.lifes)
						life_lost_sfx.play()

				if event.key == pg.K_a:
					config.moving_left = True 

				if event.key == pg.K_d:
					config.moving_right = True
				
				if event.key == pg.K_m:
					music.volume_mute()

				if event.key == pg.K_KP_PLUS:
					music.volume_plus()

				if event.key == pg.K_KP_MINUS:
					music.volume_minus()

			if event.type == pg.KEYUP:

				if event.key == pg.K_a:
					config.moving_left = False

				if event.key == pg.K_d:
					config.moving_right = False

		if config.moving_left:
			ship.move(1)

		if config.moving_right:
			ship.move(2)

		screen.blit(ig.background,(0,0))
		ship.draw(screen)
			#drawing asteroids
		for asteroid in config.Asteroids:
			asteroid.draw(screen)
			#moving and removing asteroids 
		for asteroid in config.Asteroids[:]:
			asteroid.move()
			if (asteroid.y + config.asteroid_vel) > 720:
				config.Asteroids.remove(asteroid)
				asteroid_grp.remove(asteroid)
				print(asteroid_grp)
				print("ASTEROIDS REMAINING: "+str(len(config.Asteroids)))
				if len(config.Asteroids) == 0:
					config.y_max -=	200  
					config.y_min -= 100 

		screen.blit(stage_text,(950, 10))
		screen.blit(score_text,(420,10))
		
		if pg.sprite.spritecollide(rocket_grp.sprite,asteroid_grp,False,pg.sprite.collide_mask):
			print('collided')

		for i in range(len(lifes)):	
			lifes[i].draw(screen)

		pg.display.update()

#- - - - - - GAME-OVER - - - - - - -#
	def game_over(self,screen):
		music.unload()
		screen.fill('black')
		fps.tick(frames)
		
		if config.last_score > config.high_score:
			config.high_score = config.last_score
			with open('high_score.txt', 'w') as file:
				file.write(str(config.high_score))

		game_over_text = game_font.render("PRESS ENTER TO GO BACK TO MAIN MENU", 1 , (255,255,255))
		score_text = game_font.render(f"SCORE: {config.last_score}", 1, (255,255,255))
		high_score_text = game_font.render(f"HIGH SCORE {config.high_score}", 1,(255,255,255))

		for event in pg.event.get():
			
			if event.type == pg.QUIT:
				config.game_state = False

			if event.type == pg.KEYDOWN:

				if event.key == pg.K_RETURN:
					switch_sfx.play()
					res.restart()
					res.reset()
					music.load()
					break

		screen.blit(ig.game_over,(0,0))
		screen.blit(game_over_text,(80,500))
		screen.blit(score_text,(500,580))
		screen.blit(high_score_text,(500,660))
		pg.display.update()

#obstacles
class Asteroid(pg.sprite.Sprite):
	                    
	def __init__(self,x ,y):
		pg.sprite.Sprite.__init__(self)
		self.image = ig.asteroid
		self.x = x
		self.y = y
		self.rect = self.image.get_rect(center = (self.x,self.y))
		self.mask = pg.mask.from_surface(self.image)

	def move(self):
		self.y += config.asteroid_vel

	def draw(self,screen):
		for asteroid in config.Asteroids:
			screen.blit(self.image,(self.x,self.y))

#groups:
rocket_grp = pg.sprite.GroupSingle(ship)
asteroid_grp = pg.sprite.Group()

scene = SCENE()
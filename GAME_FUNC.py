#Game functions
import pygame as pg
import os
import random
import sys
import images as ig
from images import BACK
import music
from music import *
import config
import webbrowser
from rocket import lifes
from rocket import life1
from rocket import life2
from rocket import life3
from rocket import res
from rocket import ship
#initializations
pg.font.init()
fps = pg.time.Clock()
frames = 60
window = 1
wipe = False
counter = 0

def UD():
	pg.display.update()

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
		UD()
			
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
					res.reset()
					res.restart()
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
		UD()

# - - - - - - - - MAIN-GAME - - - - - - #
	def main_game(self,screen):
		global window
		global wipe
		global counter
		global refresh 
		FPS = fps.get_fps().__int__()
		fps.tick(frames)
		if len(config.asteroid_list) == 0:
			config.stage += 1
			if config.stage != 1 and config.stage%2 != 0:
				config.spawned = False

			config.asteroid_vel = round(config.asteroid_vel+0.8,1) 
			print('SHOWER SPEED :'+str(config.asteroid_vel))
			if config.asteroid_num + config.stage >= 20:
				config.asteroid_num = 20
			else:
				config.asteroid_num += config.stage
			for i in range(config.asteroid_num):
				asteroid = Asteroid(random.randrange(0,1180), random.randrange(config.y_max,config.y_min)) 
				config.asteroid_list.append(asteroid)		 

		if len(config.power_list) == 0 and config.stage%2 == 0 and config.spawned == False:
			power = Powers(random.randrange(0,1180), random.randrange(config.y_max,config.y_min))
			config.power_list.append(power)
			print('spawned')

		screen.fill('black')
		stage_text = game_font.render(f"STAGE: {config.stage}", 1, (102,0,102))
		score_text = game_font.render(f"SCORE: {config.score}", 1, (102,0,102))
		fps_text = small_game_font.render(f"FPS: {FPS}",1,(255,255,255))
		wipe_out_text = small_game_font.render(f"WIPE OUTS: {config.powers_count}",1,(255,255,255))

		for event in pg.event.get():
			if event.type == pg.QUIT:
				config.game_state = False

			if event.type == pg.KEYDOWN:

				if event.key == pg.K_ESCAPE:
					switch_sfx.play()
					res.reset()
					res.restart()					

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

				if event.key == pg.K_SPACE and config.powers_count > 0:
					wipe = True

			if event.type == pg.KEYUP:

				if event.key == pg.K_a:
					config.moving_left = False

				if event.key == pg.K_d:
					config.moving_right = False

		BACK.moving_bg(screen,config.asteroid_vel)

		#drawing_rocket	
		config.current_rocket += 0.3
		if config.current_rocket >= 5:
			config.current_rocket = 0
			ship.animate(screen,config.current_rocket)

		else:
			ship.animate(screen,config.current_rocket)

		if config.moving_left:
			ship.move(1)

		elif config.moving_right:
			ship.move(2)
			#drawing asteroid_list
		for asteroid in config.asteroid_list:
			asteroid.draw(screen)

		for power in config.power_list:
			power.draw(screen)
			power.move()
			power.ifhit(ship)
			#moving and removing asteroid_list 
		for asteroid in config.asteroid_list:
			asteroid.move()

			if asteroid.collision(ship):
				config.asteroid_list.remove(asteroid)
				if config.lifes == 0:
					config.switch = 4
					config.last_score = config.score
					config.score = 0
					game_over_sfx.play()
					break

				else:
					config.lifes -= 1
					lifes.pop(config.lifes)
					life_lost_sfx.play()

			elif (asteroid.y + config.asteroid_vel) >= 720:
				config.asteroid_list.remove(asteroid)
				config.score += 200*config.stage
				print("ASTEROIDS REMAINING: "+str(len(config.asteroid_list)))
				if len(config.asteroid_list) == 0:
					config.y_max -=	200  
					config.y_min -= 100

		screen.blit(stage_text,(950, 10))
		screen.blit(score_text,(420,10))
		screen.blit(fps_text,(1175,680))
		screen.blit(wipe_out_text,(10,680))

		for i in range(len(lifes)):	
			lifes[i].draw(screen)

		if wipe == True:
			wipeout_sfx.play()
			config.asteroid_list.clear()
			if counter < 10000000:
				counter += 2
				pg.draw.rect(screen, (255,255,255), (0,0,1280,720))
			config.powers_count -= 1
			wipe = False
		UD()

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
					res.reset()
					res.restart()
					music.load()
					break

		screen.blit(ig.game_over,(0,0))
		screen.blit(game_over_text,(80,500))
		screen.blit(score_text,(500,580))
		screen.blit(high_score_text,(500,660))
		UD()

#obstacles
class Asteroid():
	                    
	def __init__(self,x ,y):
		pg.sprite.Sprite.__init__(self)
		self.image = ig.asteroid
		self.x = x
		self.y = y
		self.mask = pg.mask.from_surface(self.image)

	def move(self):
		self.y += config.asteroid_vel

	def draw(self,screen):
		for asteroid in config.asteroid_list:
			screen.blit(self.image,(self.x,self.y))

	def collision(self,obj):
		collide_mask = self.mask.overlap_mask(obj.mask, (self.x - obj.x, self.y - obj.y))
		if collide_mask.count() > 0:
			return True
		else:
			return False

class Powers():
		
	def __init__(self,x , y):
		self.image = random.choice(config.powers)
		self.choice = self.image
		if self.image == ig.wipeout:
			self.image = pg.transform.scale(self.image,(100,100))
		else:
			self.image = pg.transform.scale(self.image,(80,80))
		self.x = x
		self.y = y
		self.mask = pg.mask.from_surface(self.image)
		
	def move(self):
		self.y += config.asteroid_vel

	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y))		

	def ifhit(self,obj):
		collide_mask = self.mask.overlap_mask(obj.mask, (self.x - obj.x, self.y - obj.y))
		if collide_mask.count() > 0 and self.choice == ig.wipeout:
			life_gain_sfx.play()
			config.powers_count += 1
			config.power_list.clear()
			config.spawned = True

		elif collide_mask.count() > 0 and self.choice == ig.rocket:
			if len(lifes) == 3:
				print('lifes full')

			elif len(lifes) == 2:
				config.lifes += 1
				lifes.append(life3)

			elif len(lifes) == 1:
				config.lifes += 1
				lifes.append(life2)

			elif len(lifes) == 0:
				config.lifes += 1
				lifes.append(life1)

			life_gain_sfx.play()
			config.power_list.clear()
			config.spawned = True

		elif self.y + config.asteroid_vel >=720:
			config.spawned = True
			config.power_list.clear()			

scene = SCENE()
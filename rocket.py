#Rocket_object
import pygame as pg
import images as ig
import config

#Player class
class ROCKET():
	def __init__(self,x,y,size):
		self.image = ig.rocket
		self.x = x
		self.y = y
		self.size = size
		self.image = pg.transform.scale(self.image,((100*self.size), (100*self.size)))
		self.mask = pg.mask.from_surface(self.image)
		self.vel = 8

	def draw(self,screen):
		screen.blit(self.image,(self.x, self.y))

	def animate(self,screen,sprite):
		self.image = moving_rocket[int(sprite)]
		self.image = pg.transform.scale(self.image,((100*self.size), (100*self.size)))
		screen.blit(self.image,(self.x, self.y))

	def move(self,direction):
		if direction == 1 and (self.x + self.vel) > 0:
			self.x -= self.vel

		elif direction == 2 and (self.x + self.vel) < 1180:
			self.x += self.vel		

class func():

	# - - for plotting lifes - - #
	def restart(self):
		config.lifes = 3
		config.switch = 1
		lifes.append(life1)
		lifes.append(life2)
		lifes.append(life3)

	def reset(self):
		config.asteroid_list.clear()
		config.power_list.clear()
		config.powers_count = 0
		config.spawned = False
		lifes.clear()
		ship.x = 600
		ship.y = 600
		config.moving_left = False
		config.moving_right = False
		config.stage = 0
		config.score = 0
		config.asteroid_vel = 2
		config.asteroid_num = 10
		config.switch = 1
		config.y_max = -2500
		config.y_min = -200

#objects
res = func()
moving_rocket = [ig.rocket,ig.rocket1,ig.rocket2,ig.rocket1,ig.rocket2]
ship = ROCKET(600,600,1)
lifes = []
life1 = ROCKET(0,10,0.7)
life2 = ROCKET(70,10,0.7)
life3 = ROCKET(140,10,0.7)
lifes.append(life1)
lifes.append(life2)
lifes.append(life3)
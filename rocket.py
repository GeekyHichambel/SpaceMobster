#Rocket_object
import pygame as pg
import images as ig
import config

class ROCKET(pg.sprite.Sprite):
	def __init__(self,x,y,size):
		pg.sprite.Sprite.__init__(self)
		self.image = ig.rocket
		self.rect = self.image.get_rect(center = (600,600))
		self.size = size
		self.x = x
		self.y = y
		self.mask = pg.mask.from_surface(self.image)
		self.vel = 8 

	def draw(self,screen):
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
		config.Asteroids.clear()
		config.stage = 0
		config.score = 0
		config.asteroid_vel = 1
		config.asteroid_num = 10
		config.switch = 1
		config.y_max = -2500
		config.y_min = -200

#objects
res = func()
ship = ROCKET(600,600,1)
lifes = []
life1 = ROCKET(0,10,0.7)
life2 = ROCKET(70,10,0.7)
life3 = ROCKET(140,10,0.7)
lifes.append(life1)
lifes.append(life2)
lifes.append(life3)
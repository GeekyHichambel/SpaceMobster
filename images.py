#Image loading
import pygame as pg
import os

rocket = pg.image.load(os.path.join("resources","rocket.png"))
rocket1 = pg.image.load(os.path.join("resources","rocket1.png"))
rocket2 = pg.image.load(os.path.join("resources","rocket2.png"))
asteroid = pg.image.load(os.path.join("resources","asteroid.png"))
background = pg.image.load(os.path.join("resources","BG.png"))
control_button = pg.image.load(os.path.join("resources","Controlbut.png"))
control_button_2 = pg.image.load(os.path.join("resources","Controlbut(2).png"))
start_button = pg.image.load(os.path.join("resources","Startbut.png"))
start_button_2 = pg.image.load(os.path.join("resources","Startbut(2).png"))
control_screen = pg.image.load(os.path.join("resources","controlpage.jpg"))
game_over = pg.image.load(os.path.join("resources","game_over.png"))
main_menu = pg.image.load(os.path.join("resources","main_menu.jpg"))
wipeout = pg.image.load(os.path.join("resources","pow_1.png"))
white_bg = pg.image.load(os.path.join("resources","white.png"))

def perf():
	rocket.convert_alpha()
	rocket1.convert_alpha()
	rocket2.convert_alpha()
	asteroid.convert_alpha()
	background.convert_alpha()
	control_button.convert_alpha()
	control_button_2.convert_alpha()
	start_button.convert_alpha()
	start_button_2.convert_alpha()
	control_screen.convert_alpha()
	game_over.convert_alpha()
	main_menu.convert_alpha()
	wipeout.convert_alpha()
	white_bg.convert_alpha()

class back():

	def __init__(self,image):
		self.image1 = image
		self.image2 = image
		self.rect1 = self.image1.get_rect(topleft=(0,0))
		self.rect2 = self.image2.get_rect(topleft=(0,-720))

	def moving_bg(self,screen,vel):
		if self.rect2.y >= 0:
			self.rect1.y = 0
			self.rect2.y = -720
			screen.blit(self.image1,(self.rect1.x,self.rect1.y))
			screen.blit(self.image2,(self.rect2.x,self.rect2.y))
		
		else:
			self.rect1.y += vel
			self.rect2.y += vel
			screen.blit(self.image1,(self.rect1.x,self.rect1.y))
			screen.blit(self.image2,(self.rect2.x,self.rect2.y))

#Image holder for buttons
current_control = control_button
current_start = start_button
#background
BACK = back(background)
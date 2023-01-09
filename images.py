#Image loading
import pygame as pg
import os

rocket = pg.image.load(os.path.join("resources","rocket.png"))
asteroid = pg.image.load(os.path.join("resources","asteroid.png"))
background = pg.image.load(os.path.join("resources","BG.jpg"))
control_button = pg.image.load(os.path.join("resources","Controlbut.png"))
control_button_2 = pg.image.load(os.path.join("resources","Controlbut(2).png"))
start_button = pg.image.load(os.path.join("resources","Startbut.png"))
start_button_2 = pg.image.load(os.path.join("resources","Startbut(2).png"))
control_screen = pg.image.load(os.path.join("resources","controlpage.jpg"))
game_over = pg.image.load(os.path.join("resources","game_over.png"))
main_menu = pg.image.load(os.path.join("resources","main_menu.jpg"))

#Image holder for buttons
current_control = control_button
current_start = start_button
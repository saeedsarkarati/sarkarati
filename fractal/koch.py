import pygame
from pygame.locals import *
from math import *
import random
pygame.init()
sc = pygame.display.set_mode((800, 600))
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
# -----------------
x = 0; y = 0 ; l = 650
for i in range (10000):
	sc.set_at( (int(x), int(y) ), red )
	r = random.randint(0, 3)
	# ~ print (r)
	if r == 0:
		x = x / 3; y = y / 3
	if r == 1:
		x = x / 3 + l *2 / 3; y = y / 3
	if r == 2:
		theta = pi / 6
		x = x / 3 ; y = y / 3
		x, y = x * cos (theta) - y * sin (theta), y * cos (theta) + x * sin (theta)
		x += l / 3
	if r == 3:
		theta = -pi / 6
		x = x / 3 ; y = y / 3
		x, y = x * cos (theta) - y * sin (theta), y * cos (theta) + x * sin (theta)
		x += l / 2; y += l/3 * 3**.5 / 2
	
	

# ---------------
pygame.display.update()

cont = True
while cont:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == K_q:
				cont = False
		if event.type == QUIT:
			cont = False
pygame.quit()

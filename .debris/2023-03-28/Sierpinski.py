import pygame
from pygame.locals import *
import random
pygame.init()
sc = pygame.display.set_mode((800, 600))
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
# -----------------
x = 10; y = 10 ; l = 500
for i in range (100000):
	sc.set_at( (int(x), int(y) ), red )
	r = random.randint(0, 2)
	# ~ print (r)
	if r == 0:
		x = x / 2; y = y / 2
	if r == 1:
		x = x / 2 + l/2; y = y / 2
	if r == 2:
		x = x / 2 + l/4; y = y / 2 + l * 3 **0.5 / 4
	
	

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

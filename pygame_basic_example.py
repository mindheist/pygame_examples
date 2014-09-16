# import library of functions called pygame :)
import pygame
pygame.init()  # initialize pygame


BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = ( 0,0,255)
GREEN = (0,255,0)
RED   = ( 255,0,0)
size=(1670,750)  # size of the output
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	screen.fill(WHITE)
	#pygame.draw.line(screen,BLACK,[0,0],[400,400],5)
	#pygame.draw.rect(screen,BLACK,[0,0,600,200],5)
	#pygame.draw.ellipse(screen,BLACK,[0,0,600,200],5)
	pygame.draw.polygon(screen,BLACK,[[100,100],[250,250],[350,250],[550,250]],5)


	pygame.display.flip()
	clock.tick(60)

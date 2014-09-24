# A simple program to Draw Walls for my game 
# Goal : To understand how sprites works and are implemented

import pygame

#=== DEFINE COLORS ====#

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#=========================#

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#=========================#
class Wall (pygame.sprite.Sprite):
	#== The wall is going to have origin co-ordinates (x and y) , height and width 
	def __init__(self,x,y,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		#=== The above line actually draws a surface ====#
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
wall_list = pygame.sprite.Group()

wall_top = Wall (0 ,0 ,800 ,10)
wall_list.add(wall_top)

wall_left = Wall(0,0,10,800)
wall_list.add(wall_left)

wall_bottom = Wall (0, 790,800,10)
wall_list.add(wall_bottom)
clock = pygame.time.Clock()

wall_right = Wall ( 790,0,10,800)
wall_list.add(wall_right)
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	wall_list.draw(screen)

	

	
	pygame.display.flip()

	clock.tick(60)

pygame.quit()












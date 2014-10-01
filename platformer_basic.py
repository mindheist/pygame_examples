

#== 1. Import the pygame library
import pygame
#=== 2. Define colors ,screen width and height, Clock
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

clock = pygame.time.Clock()
# == This will tick 60 times a minute later in the main loop

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#============================================================

class Player (pygame.sprite.Sprite):
	"""This is the Player class,this is a sub class of the sprite superclass"""
	"""Call the contructor of this class"""
	def __init__(self):
		"""Call the contructor of the super class now"""
		pygame.sprite.Sprite.__init__(self)
		""" Draw the Player now into the surface and assign it to image"""
		width = 40
		height = 60 
		""" In the program , we already specify the width and height of the Player"""
		self.image = pygame.Surface([width,height])
		self.image.fill(RED)
		self.rect = self.image.get_rect()



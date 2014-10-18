# import Libraries

import pygame
import random
import time

# DEFINE COLORS

BLACK = ( 0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

# SCREEN SIZE

screen_width = 1500
screen_height = 1000

#Clock

clock = pygame.time.Clock()

class Star(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

def main():
	
	pygame.init()

	screen = pygame.display.set_mode([screen_width,screen_height])

	background = pygame.image.load("kepler1.jpg").convert()
	background.set_colorkey(WHITE)

	alien1 = pygame.image.load("alien1.jpg").convert()
	#alien1.set_colorkey(WHITE)
	catastrophes_sprite = pygame.image.load("catastrophes.png").convert()


	basicfont = pygame.font.SysFont(None, 30)
	text = basicfont.render('Pandemic', True, BLUE, BLACK)
	textRect=text.get_rect()
	textRect.x = 1
	textRect.y = 1

	basicfont = pygame.font.SysFont(None, 30)
	text2 = basicfont.render('Famine', True, BLUE, BLACK)
	textRect2=text2.get_rect()
	textRect2.x = 2
	textRect2.y = 31

	basicfont = pygame.font.SysFont(None, 30)
	text3 = basicfont.render('Pollution', True, BLUE, BLACK)
	textRect3=text3.get_rect()
	textRect3.x = 3
	textRect3.y = 62

	basicfont = pygame.font.SysFont(None, 30)
	text4 = basicfont.render('War', True, BLUE, BLACK)
	textRect4=text4.get_rect()
	textRect4.x = 4
	textRect4.y = 93


	star_list = pygame.sprite.Group()

	all_sprites_list = pygame.sprite.Group()
     
	star =Star ( GREEN,5,5)
	star.rect.x = 250
	star.rect.y = 250
	star_list.add(star)
	all_sprites_list.add(star)

	
	for i in range(70):
		star = Star(RED,5,5)
		star.rect.x = random.randrange(200,700)
		star.rect.y = random.randrange(53,543)
		star_list.add(star)
		all_sprites_list.add(star)

	screen.blit(background,(0,0))
	screen.blit(text,textRect)
	screen.blit(text2,textRect2)
	screen.blit(text3,textRect3)
	#screen.blit(text4,textRect4)
	screen.blit(catastrophes_sprite,(0,0))
	all_sprites_list.draw(screen)

	done = False

	# print all the star postions for debugging

	#for star in star_list:
	#	print star.rect.x , star.rect.y

	score = 0

	while not done :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				clicked_sprite = [s for s in star_list if s.rect.collidepoint(pos)]
				print clicked_sprite 
				for s in clicked_sprite:
					print s.rect.x , s.rect.y
					if s.rect.x ==250 and s.rect.y == 250:
						print "Green Sprite"
						screen.blit(background,(0,0))
						
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						#screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(0,0))
						all_sprites_list.draw(screen)
						
						screen.blit(alien1,(1200,1))
							


		clock.tick(60)

		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()



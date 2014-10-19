# import Libraries

import pygame
import random
import time
import pygbutton
import sys

# DEFINE COLORS

BLACK  = (  0,  0,  0)
WHITE  = (255,255,255)
RED    = (255,  0,  0)
GREEN  = (  0,255,  0)
BLUE   = (  0,  0,255)
MAROON = (128,  0,  0)

# SCREEN SIZE

screen_width = 1500
screen_height = 1000

#Clock

clock = pygame.time.Clock()

menu_font = pygame.font.Font(None, 40)

class Star(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

	
def main():
	
	pygame.init()

	screen = pygame.display.set_mode([screen_width,screen_height])

	background = pygame.image.load("kepler-dark.jpg").convert()
	background.set_colorkey(WHITE)


	star1 = pygame.image.load("star1.jpg").convert()
	star2 = pygame.image.load("star2.jpg").convert()
	star3 = pygame.image.load("star3.jpg").convert()
	star4 = pygame.image.load("star4.jpg").convert()
	star5 = pygame.image.load("star5.jpg").convert()

	contact1 = pygame.image.load("contact1.jpg").convert()

	alien1 = pygame.image.load("alien1.jpg").convert()

	catastrophes_sprite = pygame.image.load("catastrophes.png").convert()


	basicfont = pygame.font.SysFont(None, 20)
	text = basicfont.render('PANDEMIC', True, WHITE, BLACK)
	textRect=text.get_rect()
	textRect.x = 1
	textRect.y = 10

	basicfont = pygame.font.SysFont(None, 20)
	text2 = basicfont.render('FAMINE', True, WHITE, BLACK)
	textRect2=text2.get_rect()
	textRect2.x = 2
	textRect2.y = 31

	basicfont = pygame.font.SysFont(None, 20)
	text3 = basicfont.render('POLLUTION', True, WHITE, BLACK)
	textRect3=text3.get_rect()
	textRect3.x = 3
	textRect3.y = 52

	basicfont = pygame.font.SysFont(None, 20)
	text4 = basicfont.render('WAR', True, WHITE, BLACK)
	textRect4=text4.get_rect()
	textRect4.x = 4
	textRect4.y = 73

	basicfont = pygame.font.SysFont(None, 30)
	menu_text_1 = basicfont.render('BIG BANG THEORY', True, GREEN, BLACK)
	menutextRect1=menu_text_1.get_rect()
	menutextRect1.x = 1150
	menutextRect1.y = 610

	menu_text_2 = basicfont.render('NUCLEAR FISSION', True, GREEN, BLACK)
	menutextRect2=menu_text_2.get_rect()
	menutextRect2.x = 1150
	menutextRect2.y = 650

	menu_text_3 = basicfont.render('EVOLUTION/NATURAL SELECTION', True, GREEN, BLACK)
	menutextRect3=menu_text_3.get_rect()
	menutextRect3.x = 1150
	menutextRect3.y = 690

	menu_text_4 = basicfont.render('CLOUD COMPUTING', True, GREEN, BLACK)
	menutextRect4=menu_text_4.get_rect()
	menutextRect4.x = 1150
	menutextRect4.y = 730

	"""
	text_array = ['POETRY', 'CULTURE' , 'DANCE' , 'FILM']
	menu_text = []
	menutextRect = []

	for i in range (1,4):
		menu_text[i] = basicfont.render( text_array[i],True,GREEN,BLACK)
		menutextRect[i] = menu_text[i].get_rect()
		menutextRect[i].x = 1150
		menutextRect[i].y = 730 + (i*40)
	"""

	menu_text_5 = basicfont.render('DANCE', True, GREEN, BLACK)
	menutextRect5=menu_text_5.get_rect()
	menutextRect5.x = 1150
	menutextRect5.y = 770

	menu_text_6 = basicfont.render('FILM', True, GREEN, BLACK)
	menutextRect6=menu_text_6.get_rect()
	menutextRect6.x = 1150
	menutextRect6.y = 810

	menu_text_7 = basicfont.render('SEND', True, GREEN, BLACK)
	menutextRect7=menu_text_7.get_rect()
	menutextRect7.x = 1300
	menutextRect7.y = 900

	basicfont = pygame.font.SysFont(None, 40)
	menu_text_9 = basicfont.render('MESSAGE SENT', True, GREEN, BLACK)
	menutextRect9=menu_text_9.get_rect()
	menutextRect9.x = 1200
	menutextRect9.y = 900

	star_list = pygame.sprite.Group()

	all_sprites_list = pygame.sprite.Group()
     
	star =Star ( GREEN, 7, 7)
	star.rect.x = 750
	star.rect.y = 250
	star_list.add(star)
	all_sprites_list.add(star)

	star = Star(GREEN, 7, 7)
	star.rect.x = 500
	star.rect.y = 200
	star_list.add(star)
	all_sprites_list.add(star)

	star = Star ( GREEN, 5 , 5)
	star.rect.x = 850
	star.rect.y = 300
	star_list.add(star)
	all_sprites_list.add(star)

	star = Star ( GREEN, 5 , 5)
	star.rect.x = 750
	star.rect.y = 350
	star_list.add(star)
	all_sprites_list.add(star)

	star = Star ( GREEN, 5 , 5)
	star.rect.x = 600
	star.rect.y = 500
	star_list.add(star)
	all_sprites_list.add(star)
	
	for i in range(70):
		star = Star(RED,5,5)
		star.rect.x = random.randrange(500,1000)
		star.rect.y = random.randrange(53,543)
		star_list.add(star)
		all_sprites_list.add(star)

	screen.blit(background,(0,0))
	screen.blit(text,textRect)
	screen.blit(text2,textRect2)
	screen.blit(text3,textRect3)
	screen.blit(text4,textRect4)
	screen.blit(catastrophes_sprite,(110,10))
	all_sprites_list.draw(screen)

	done = False

	# print all the star postions for debugging

	#for star in star_list:
	#	print star.rect.x , star.rect.y

	score = 0

# === Step 1 : 

	while not done :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				print pos
				clicked_sprite = [s for s in star_list if s.rect.collidepoint(pos)]
				print clicked_sprite 
				for s in clicked_sprite:
					print s.rect.x , s.rect.y
					if s.rect.x ==750 and s.rect.y == 250:
						print "Green Sprite"
						screen.blit(background,(0,0))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star1,(1150,1))


					elif s.rect.x ==500 and s.rect.y ==200 :
						screen.blit(background,(0,0))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star2,(1150,1))

					elif s.rect.x ==850 and s.rect.y ==300 :
						screen.blit(background,(0,0))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star3,(1150,1))

					elif s.rect.x ==750 and s.rect.y ==350 :
						screen.blit(background,(0,0))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star4,(1150,1))

					elif s.rect.x ==600 and s.rect.y ==500 :
						screen.blit(background,(0,0))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star5,(1150,1))

					elif s.rect.x != 0 and s.rect.y != 0:
						screen.blit(background,(0,0))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						pygame.draw.rect(screen,WHITE, (1150,1,350,100))
						pygame.draw.rect(screen,GREEN, (1150,101,350,300))
						pygame.draw.rect(screen,MAROON,(1150,401,350,100))

				if (pos[0] >= 1189 and pos[0] <= 1289) and (pos[1] >=445 and pos[1]<=472):
					screen.blit(background,(0,0))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(star1,(1150,1))
					pygame.draw.rect(screen,MAROON,(1150,601,350,500))
					screen.blit(menu_text_1,menutextRect1)
					screen.blit(menu_text_2,menutextRect2)
					screen.blit(menu_text_3,menutextRect3)
					screen.blit(menu_text_4,menutextRect4)
					screen.blit(menu_text_5,menutextRect5)
					screen.blit(menu_text_6,menutextRect6)
					screen.blit(menu_text_7,menutextRect7)
					#screen.blit(alien1,(1150,520))




				if (pos[0] >= 1300 and pos[0] <= 1350):
					screen.blit(background,(0,0))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(star1,(1150,1))
					pygame.draw.rect(screen,MAROON,(1150,601,350,500))

					pygame.time.wait(1000)

					#screen.blit(menu_text_8,menutextRect8)
					screen.blit(menu_text_9,menutextRect9)

					#pygame.time.wait(5000)

					#screen.blit(contact1,(1,521))

					







		clock.tick(60)

		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()



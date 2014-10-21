# import Libraries

import pygame
import random
import time
import sys
import pygame.mixer


# DEFINE COLORS

BLACK  = (  0,  0,  0)
WHITE  = (255,255,255)
RED    = (255,  0,  0)
GREEN  = (  0,255,  0)
BLUE   = (  0,  0,255)
MAROON = (128,  0,  0)

pygame.mixer.pre_init(44100, -16, 2, 1024)
#pygame.mixer.init(44050, -16, 2, 2048)

# SCREEN SIZE

screen_width = 1500
screen_height = 1000

#Clock

clock = pygame.time.Clock()

#menu_font = pygame.font.Font(None, 40)

class Star(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

	
def main():
	
	pygame.init()
	bgm = pygame.mixer.Sound('motion.mp3')

	screen = pygame.display.set_mode([screen_width,screen_height])

	background = pygame.image.load("kepler-dark.jpg").convert()
	background.set_colorkey(WHITE)


	star1 = pygame.image.load("star1.jpg").convert()
	star2 = pygame.image.load("star2.jpg").convert()
	star3 = pygame.image.load("star3.jpg").convert()
	star4 = pygame.image.load("star4.jpg").convert()
	star5 = pygame.image.load("star5.jpg").convert()

	contact1 = pygame.image.load("contact1.jpg").convert()
	contact2 = pygame.image.load("contact2.jpg").convert()
	contact3 = pygame.image.load("contact3.jpg").convert()
	contact4 = pygame.image.load("contact4.jpg").convert()
	contact5 = pygame.image.load("contact5.jpg").convert()

	treasury_button = pygame.image.load("treasury-button.png").convert()
	knowledge_button = pygame.image.load("knowledge-button.png").convert()
	advanced_Knowledge_button = pygame.image.load("AdvancedK-button.png").convert()
	contacts_button = pygame.image.load("Contacts-button.png").convert()
	

	treasury_popup = pygame.image.load("treasury-popup.jpg").convert()
	contacts_popup = pygame.image.load("contacts-popup.jpg").convert()
	advanced_popup = pygame.image.load("advanced-k-popup.jpg").convert()


	knowledge = pygame.image.load("knowledge.jpg").convert()
	message_sent = pygame.image.load("message-sent.jpg").convert()

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
	screen.blit(treasury_button,(10,200))
	screen.blit(knowledge_button,(10,250))
	screen.blit(advanced_Knowledge_button,(10,300))
	screen.blit(contacts_button,(10,350))
	all_sprites_list.draw(screen)

	done = False

	# print all the star postions for debugging

	#for star in star_list:
	#	print star.rect.x , star.rect.y

	score = 0

	current_star = None

# === Step 1 : 

	while not done :
		bgm.play()
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
						current_star = 1
						screen.blit(background,(0,0))
						screen.blit(treasury_button,(10,200))
						screen.blit(knowledge_button,(10,250))
						screen.blit(advanced_Knowledge_button,(10,300))
						screen.blit(contacts_button,(10,350))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star1,(1150,1))


					elif s.rect.x ==500 and s.rect.y ==200 :
						current_star = 2
						screen.blit(background,(0,0))
						screen.blit(treasury_button,(10,200))
						screen.blit(knowledge_button,(10,250))
						screen.blit(advanced_Knowledge_button,(10,300))
						screen.blit(contacts_button,(10,350))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star2,(1150,1))

					elif s.rect.x ==850 and s.rect.y ==300 :
						current_star = 3
						screen.blit(background,(0,0))
						screen.blit(treasury_button,(10,200))
						screen.blit(knowledge_button,(10,250))
						screen.blit(advanced_Knowledge_button,(10,300))
						screen.blit(contacts_button,(10,350))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star3,(1150,1))

					elif s.rect.x ==750 and s.rect.y ==350 :
						current_star = 4
						screen.blit(background,(0,0))
						screen.blit(treasury_button,(10,200))
						screen.blit(knowledge_button,(10,250))
						screen.blit(advanced_Knowledge_button,(10,300))
						screen.blit(contacts_button,(10,350))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star4,(1150,1))

					elif s.rect.x ==600 and s.rect.y ==500 :
						current_star = 5 
						screen.blit(background,(0,0))
						screen.blit(treasury_button,(10,200))
						screen.blit(knowledge_button,(10,250))
						screen.blit(advanced_Knowledge_button,(10,300))
						screen.blit(contacts_button,(10,350))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						screen.blit(star5,(1150,1))

					elif s.rect.x != 0 and s.rect.y != 0:
						current_star = 100
						screen.blit(background,(0,0))
						screen.blit(treasury_button,(10,200))
						screen.blit(knowledge_button,(10,250))
						screen.blit(advanced_Knowledge_button,(10,300))
						screen.blit(contacts_button,(10,350))
						screen.blit(text,textRect)
						screen.blit(text2,textRect2)
						screen.blit(text3,textRect3)
						screen.blit(text4,textRect4)
						screen.blit(catastrophes_sprite,(110,10))
						all_sprites_list.draw(screen)
						pygame.draw.rect(screen,WHITE, (1150,1,350,100))
						pygame.draw.rect(screen,GREEN, (1150,101,350,300))
						pygame.draw.rect(screen,MAROON,(1150,401,350,100))

				if (pos[0] >= 1189 and pos[0] <= 1289) and (pos[1] >=445 and pos[1]<=472) and (current_star == 1):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)    #Pandemic
					screen.blit(text2,textRect2)  #Famine
					screen.blit(text3,textRect3)  #Pollution
					screen.blit(text4,textRect4)  #War
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(star1,(1150,1))
					screen.blit(knowledge,(1150,505)) # verifying this line
					break
					#pygame.draw.rect(screen,MAROON,(1150,601,350,500))
					#screen.blit(menu_text_1,menutextRect1) #BigBang
					#screen.blit(menu_text_2,menutextRect2) # Nuclear Fission
					#screen.blit(menu_text_3,menutextRect3) # Evolution / Natural Selection
					#screen.blit(menu_text_4,menutextRect4) # Cloud Computing
					#screen.blit(menu_text_5,menutextRect5) # Dance 
					#screen.blit(menu_text_6,menutextRect6) # Film
					#screen.blit(menu_text_7,menutextRect7) # Send
					#screen.blit(alien1,(1150,520))


				if (pos[0] >= 1190 and pos[0] <= 1300) and (pos[1] >=952 and pos[1]<=980) and (current_star == 1):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					#screen.blit(star1,(1150,1))
					#pygame.draw.rect(screen,MAROON,(1150,601,350,500))

					pygame.time.delay(1000)

					screen.blit(message_sent,(1150,525))

				
				if (pos[0] >= 1406  and pos[0]<= 1468 ) and (pos[1]>=540 and pos[1]<= 570 ) and (current_star == 1):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					pygame.time.delay(2000)
					screen.blit(contact1,(1,521)) # first alien contact

				if (pos[0] >= 40  and pos[0]<= 140 ) and (pos[1]>=964 and pos[1]<= 994 ) and (current_star ==1 ):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen) 

# second star workflow			

				if (pos[0] >= 1189 and pos[0] <= 1289) and (pos[1] >=445 and pos[1]<=472) and (current_star == 2):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)    #Pandemic
					screen.blit(text2,textRect2)  #Famine
					screen.blit(text3,textRect3)  #Pollution
					screen.blit(text4,textRect4)  #War
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(star2,(1150,1))
					screen.blit(knowledge,(1150,505))
					break
					

				if (pos[0] >= 1190 and pos[0] <= 1300) and (pos[1] >=952 and pos[1]<=980) and (current_star == 2):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					#screen.blit(star1,(1150,1))
					#pygame.draw.rect(screen,MAROON,(1150,601,350,500))

					pygame.time.delay(1000)

					screen.blit(message_sent,(1150,525))

				
				if (pos[0] >= 1406  and pos[0]<= 1468 ) and (pos[1]>=540 and pos[1]<= 570 ) and (current_star == 2):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					pygame.time.delay(2000)
					screen.blit(contact2,(1,521)) # first alien contact

				if (pos[0] >= 40  and pos[0]<= 140 ) and (pos[1]>=964 and pos[1]<= 994 ) and (current_star ==2 ):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)

# Third Star

				if (pos[0] >= 1189 and pos[0] <= 1289) and (pos[1] >=445 and pos[1]<=472) and (current_star == 3):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)    #Pandemic
					screen.blit(text2,textRect2)  #Famine
					screen.blit(text3,textRect3)  #Pollution
					screen.blit(text4,textRect4)  #War
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(star3,(1150,1))
					screen.blit(knowledge,(1150,505))
					break
					

				if (pos[0] >= 1190 and pos[0] <= 1300) and (pos[1] >=952 and pos[1]<=980) and (current_star == 3):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					#screen.blit(star3,(1150,1))
					#pygame.draw.rect(screen,MAROON,(1150,601,350,500))

					pygame.time.delay(500)

					screen.blit(message_sent,(1150,525))

				
				if (pos[0] >= 1406  and pos[0]<= 1468 ) and (pos[1]>=540 and pos[1]<= 570 ) and (current_star == 3):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					pygame.time.delay(2000)
					screen.blit(contact3,(1,521)) # first alien contact

				if (pos[0] >= 40  and pos[0]<= 140 ) and (pos[1]>=964 and pos[1]<= 994 ) and (current_star == 3 ):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)

# 4th star
				
				if (pos[0] >= 1189 and pos[0] <= 1289) and (pos[1] >=445 and pos[1]<=472) and (current_star == 4):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)    #Pandemic
					screen.blit(text2,textRect2)  #Famine
					screen.blit(text3,textRect3)  #Pollution
					screen.blit(text4,textRect4)  #War
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(star4,(1150,1))
					screen.blit(knowledge,(1150,505))
					break
				


				if (pos[0] >= 1190 and pos[0] <= 1300) and (pos[1] >=952 and pos[1]<=980) and (current_star == 4):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					#screen.blit(star1,(1150,1))
					#pygame.draw.rect(screen,MAROON,(1150,601,350,500))

					pygame.time.delay(1000)

					screen.blit(message_sent,(1150,525))

				
				if (pos[0] >= 1406  and pos[0]<= 1468 ) and (pos[1]>=540 and pos[1]<= 570 ) and (current_star == 4):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))

					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					pygame.time.delay(2000)
					screen.blit(contact4,(1,521)) # alien contact

				if (pos[0] >= 40  and pos[0]<= 140 ) and (pos[1]>=964 and pos[1]<= 994 ) and (current_star == 4 ):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)

# 5th star

				if (pos[0] >= 1189 and pos[0] <= 1289) and (pos[1] >=445 and pos[1]<=472) and (current_star == 5):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)    #Pandemic
					screen.blit(text2,textRect2)  #Famine
					screen.blit(text3,textRect3)  #Pollution
					screen.blit(text4,textRect4)  #War
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(star5,(1150,1))
					screen.blit(knowledge,(1150,505))
					break

				if (pos[0] >= 1190 and pos[0] <= 1300) and (pos[1] >=952 and pos[1]<=980) and (current_star == 5):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					#screen.blit(star1,(1150,1))
					#pygame.draw.rect(screen,MAROON,(1150,601,350,500))

					pygame.time.delay(1000)

					screen.blit(message_sent,(1150,525))

				
				if (pos[0] >= 1406  and pos[0]<= 1468 ) and (pos[1]>=540 and pos[1]<= 570 ) and (current_star == 5):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					pygame.time.delay(2000)
					screen.blit(contact5,(1,521)) # first alien contact

				if (pos[0] >= 40  and pos[0]<= 140 ) and (pos[1]>=964 and pos[1]<= 994 ) and (current_star == 5 ):
					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))		
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)

# Treasury Pop-up blitting below

				if (pos[0] >= 10 and pos[0] <= 52 ) and (pos[1] >=200 and pos[1]<=242) :

					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))		
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(treasury_popup,(100,150))


# Knowledge pop-up Blitting below


				if (pos[0] >= 10 and pos[0] <= 52 ) and (pos[1] >=252 and pos[1]<=292) :

					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))		
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(knowledge,(100,150))

# Advanced Knowledge popup Blitting below


				if (pos[0] >= 10 and pos[0] <= 52 ) and (pos[1] >=302 and pos[1]<=341) :

					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))		
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(advanced_popup,(100,150))

# Contacts popup blitted here


				if (pos[0] >= 10 and pos[0] <= 52 ) and (pos[1] >=351 and pos[1]<=391) :

					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))		
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					screen.blit(contacts_popup,(100,150))

# Close pop-ups

				if (pos[0] >= 138 and pos[0] <= 248 ) and (pos[1] >= 596 and pos[1]<= 625) :

					screen.blit(background,(0,0))
					screen.blit(treasury_button,(10,200))
					screen.blit(knowledge_button,(10,250))
					screen.blit(advanced_Knowledge_button,(10,300))
					screen.blit(contacts_button,(10,350))		
					screen.blit(text,textRect)
					screen.blit(text2,textRect2)
					screen.blit(text3,textRect3)
					screen.blit(text4,textRect4)
					screen.blit(catastrophes_sprite,(110,10))
					all_sprites_list.draw(screen)
					

		clock.tick(60)

		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()



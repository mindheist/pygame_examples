# A simple program to Draw Walls for my game 
# Goal : To understand how sprites works and are implemented
# Also adding a quick link to the Game Loop Document about how to think like 
# a computer scientist :
# 17.1 Here desribes a Game Loop : 
# http://openbookproject.net/thinkcs/python/english3e/pygame.html
#       Poll And Handle Events from the user
#                 ||
#                 ||
#   Update the game elements 
#                 ||
#   Draw the elements on the surface
#                 ||
#   Show the elements on the surface ( pygame.display.flip)


import pygame

#=== DEFINE COLORS ====#

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
GREY  = (84,84,84)

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

#=========================#

class Player ( pygame.sprite.Sprite):
	# properties of the player would be coded here
	# first draw the player ( which is basically a small white box)

	change_x = 0
	change_y = 0

	def __init__(self,x,y,n):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([n,n])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def ChangeSpeed(self,x,y):
		self.change_x = self.change_x + x
		self.change_y = self.change_y + y 

	def update(self,Walls):

		self.rect.x += self.change_x
# === The following code makes the wall opaque ; the way the walls are made 
# === opaque is a redraw trick (just like how a moving sprite is also a redraw trick)
# === A moving box is nothing but a repeatedly drawn box one-next-to-the-other
# === To achieve opaqueness of the wall , we basically redraw the box at the 
# === intersection of the wall and the player repeatedly

		block_hit_list = pygame.sprite.spritecollide(self,Walls,False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0 :
				self.rect.left = block.rect.right

		self.rect.y += self.change_y
		block_hit_list = pygame.sprite.spritecollide(self,Walls,False)
		for block in block_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top 
			else :
				self.rect.top = block.rect.bottom



pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])


wall_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

wall_top = Wall (0 ,0 ,800 ,10)
wall_list.add(wall_top)
all_sprite_list.add(wall_top)

wall_left = Wall(0,0,10,800)
wall_list.add(wall_left)
all_sprite_list.add(wall_left)

wall_bottom = Wall (0, 790,800,10)
wall_list.add(wall_bottom)
all_sprite_list.add(wall_bottom)
clock = pygame.time.Clock()

wall_right = Wall ( 790,0,10,800)
wall_list.add(wall_right)
all_sprite_list.add(wall_right)

#wall_median = Wall ( 100,400,400,10)
#wall_list.add(wall_median)

player = Player(20,20,10)
all_sprite_list.add(player)

done = False

# Game Loop has 4 Steps : Step 1 : Poll for inputs and handle them

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.ChangeSpeed(-10,0)
			elif event.key == pygame.K_RIGHT:
				player.ChangeSpeed(10,0)
			elif event.key == pygame.K_UP:
				player.ChangeSpeed(0,-5)
			elif event.key == pygame.K_DOWN:
				player.ChangeSpeed(0,5)

		elif event.type ==pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.ChangeSpeed(10,0)
			elif event.key == pygame.K_RIGHT:
				player.ChangeSpeed(-10,0)
			elif event.key ==pygame.K_UP:
				player.ChangeSpeed(0,5)
			elif event.key == pygame.K_DOWN:
				player.ChangeSpeed(0,-5)

# Game Loop has 4 Steps : Step 2: Update the player's position (wrt) the Walls
  

	player.update(wall_list)

# Game Loop has 4 Steps : Step 3: Draw the Surface

	screen.fill(GREY)
	all_sprite_list.draw(screen)

# Game Loop has 4 Steps : Step 4 : Show the stuff that has just been drawn 

	pygame.display.flip()

	clock.tick(60)

pygame.quit()












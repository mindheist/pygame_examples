# A simple program to Draw Walls for my game 
# Goal : To understand how sprites works and are implemented
import pygame

#=== DEFINE COLORS ====#

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

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
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.ChangeSpeed(-5,0)
			elif event.key == pygame.K_RIGHT:
				player.ChangeSpeed(5,0)
			elif event.key == pygame.K_UP:
				player.ChangeSpeed(0,-5)
			elif event.key == pygame.K_DOWN:
				player.ChangeSpeed(0,5)

		elif event.type ==pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.ChangeSpeed(5,0)
			elif event.key == pygame.K_RIGHT:
				player.ChangeSpeed(-5,0)
			elif event.key ==pygame.K_UP:
				player.ChangeSpeed(0,5)
			elif event.key == pygame.K_DOWN:
				player.ChangeSpeed(0,-5)
  
	# Understand the order below #	
	player.update(wall_list)
	screen.fill(BLACK)
	all_sprite_list.draw(screen)
	pygame.display.flip()

	clock.tick(60)

pygame.quit()












#== http://www.sears.com/nintendo-boy-s-graphic-t-shirt-pikachu/p-040VA71179812P
#== https://www.youtube.com/watch?v=bMt47wvK6u0
#== http://higherorderfun.com/blog/
#== http://openbookproject.net/thinkcs/python/english3e/index.html
#== http://programarcadegames.com/python_examples/show_file.php?file=platform_jumper.py

#== http://www.gilt.com/look/?s_id=dfbd312e324f9b33b4bf6f027246d5f6f00593524b58da205ebd56e79f1f2b67_0_1033759382&utm_source=gilt&utm_medium=email
#== &utm_campaign=visitrec_09302014&lk=1004479233amlf7dym7ltrdg326aq9d44awf9lvz
#== Tommy Ref blog : http://supermeatboy.com/134/How_do_I_get_started_programming_games___/
#== There is a difference in the way we need to think 
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

	change_x = 0
	change_y = 0
# A quick change from the previous maze runner example is that ; the view has changed;
# The maze runner has a view from the top of the maze;
# The platformer has a sideways view ; and also we need to include the concept of gravity

	"""This is the Player class,this is a sub class of the sprite superclass"""
	"""Call the contructor of this class"""
	def __init__(self):
		"""Call the contructor of the super class now"""
		pygame.sprite.Sprite.__init__(self)
#== Draw the Player now into the surface and assign it to image
		width = 40
		height = 40 
		""" In the program , we already specify the width and height of the Player"""
		self.image = pygame.Surface([width,height])
		self.image.fill(RED)
		self.rect = self.image.get_rect()

	def update(self):
		"""Move the Player"""
		#gravity
		self.calc_gravity()

		#Move up and Down
		self.rect.x = self.rect.x + self.change_x

	    #once we hit a wall , detect collision
		block_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
		for block in block_hit_list:
			if self.change_x > 0 :
				self.rect.right = block.rect.left
			else :
				self.rect.left = block.rect.right
# Move along the y-axis

		self.rect.y = self.rect.y + self.change_y
		
		block_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
		for  block in block_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom

	def calc_gravity(self):

			#if self.change_y ==0:   # This is a fix for moving platforms 
			#	self.change_y = 1
			#else:
			self.change_y += .35

		#See if we are on the ground - Try to Understand how this works;

			if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
				self.change_y = 0
				self.rect.y = SCREEN_HEIGHT - self.rect.height

	def jump(self):
		""" Actions when the user hits the Jump button,let me come back to this
		after writing the platform class; should jump be a single button or 
		should it be a combination of right arrow and up arrow ? """
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
		if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.change_y = -10

	def go_left(self):
		""" Move left by 6 pixels ? Find out what the accurate metric is
		This is called when the user hits the left button"""
		self.change_x = self.change_x -6

	def go_right(self):
		"""Move right by 6 pxls. This is called when the user hits the right arrow"""
		self.change_x = self.change_x + 6

	def stop(self):
		"""Called when the user lets go of the left or rightkey
		This would go in the KEYUP block later on in the code"""
		self.change_x = 0

class Platform(pygame.sprite.Sprite):

	#== Platform objects are created using this
	def __init__(self,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(GREEN)

		self.rect = self.image.get_rect()
		#self.rect.x = x
		#self.rect.y = y

#== Keep an eye on the above Class
#== Why do we pass an Object here ?
class Level(object):
	#== This is not a sprite ; and is a generic super class for all Levels
	#== Remember this common philosophy of using Lists for the objects you draw on the screen
	#== All the Walls we drew in maze_runner were added to a common list
	#== In this , we would add all the platforms we drew to a platform list.
	platform_list = None
	enemy_list    = None 
	""" There are no enemies in the game yet"""

	background = None

	def __init__(self,player):
		self.platform_list = pygame.sprite.Group()
		self.enemy_list    = pygame.sprite.Group()
		self.player        = player


	def update(self):
		self.platform_list.update()
		self.enemy_list.update()


	def draw(self,screen):
		screen.fill(BLUE)
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)

class Level_01(Level):
	def  __init__(self,player):
		Level.__init__(self,player)

		level=[[210,50,500,500],
			   [210,50,200,400],
			   [210,50,600,300],
			   [210,50,20,120],
			   [210,50,200,200]
				]

		for platform in level:
			block = Platform(platform[0],platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player #==Why do we need this
			self.platform_list.add(block)

def main():
    #== Initialize pygame , set_mode for the display and set caption
	pygame.init()
	screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
	pygame.display.set_caption("Platform Jumper")
    #== Create a player Object
	player = Player()
    
    #== Create a level list ; this will hold the levels ; right now we have only one Level   
	level_list = []
	level_list.append(Level_01(player))

	current_level_no = 0
	current_level = level_list[current_level_no]
     
    #=== Creating an Active_Sprite_List that will contain the player to start off with 
	active_sprite_list = pygame.sprite.Group()
	player.level = current_level

	player.rect.x = 340
	player.rect.y = SCREEN_HEIGHT - player.rect.height
	active_sprite_list.add(player)

	done = False
#-------- Main Program Loop ---------#

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.go_left()
				if event.key ==pygame.K_RIGHT:
					player.go_right()
				if event.key == pygame.K_UP:
					player.jump()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.change_x < 0 :
					player.stop()
				elif event.key ==pygame.K_RIGHT and player.change_x > 0:
					player.stop()

		active_sprite_list.update()
		current_level.update()

		if player.rect.right > SCREEN_WIDTH:
			player.rect.right = SCREEN_WIDTH

		if player.rect.left <0:
			player.rect.left = 0

		current_level.draw(screen)
		active_sprite_list.draw(screen)

		pygame.display.flip()

		clock.tick(60)

	pygame.quit()

if __name__ == "__main__":
	main()


					
				
				
		

		
			

		


			



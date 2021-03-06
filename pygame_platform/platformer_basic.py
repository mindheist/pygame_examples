#== http://www.sears.com/nintendo-boy-s-graphic-t-shirt-pikachu/p-040VA71179812P
#== https://www.youtube.com/watch?v=bMt47wvK6u0
#== http://higherorderfun.com/blog/
#== http://openbookproject.net/thinkcs/python/english3e/index.html
#== http://programarcadegames.com/python_examples/show_file.php?file=platform_jumper.py
#== Tommy Ref blog : http://supermeatboy.com/134/How_do_I_get_started_programming_games___/
#== There is a difference in the way we need to think
#== 1. Import the pygame library
import pygame
import pygame.mixer

from spritesheet_function import SpriteSheet
#=== 2. Define colors ,screen width and height, Clock
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
YELLOW= (255, 255,   0)

#pygame.mixer.init(21050, -16, 2, 2048)

#bgm.play()


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

	walking_frames_left = []
	walking_frames_right = []

	direction = "R"


	"""This is the Player class,this is a sub class of the sprite superclass"""
	"""Call the contructor of this class"""
	def __init__(self):

		"""Call the contructor of the super class now"""
		pygame.sprite.Sprite.__init__(self)
		sprite_sheet = SpriteSheet("p1_walk.png")
		image = sprite_sheet.get_image(0,0,66,90)
		self.walking_frames_right.append(image)
		image = sprite_sheet.get_image(66,0,66,90)
		self.walking_frames_right.append(image)

		image = sprite_sheet.get_image(132,0,67,90)
		self.walking_frames_right.append(image)

		image = sprite_sheet.get_image(0,93,66,90)
		self.walking_frames_right.append(image)

		image = sprite_sheet.get_image(66,93,66,90)
		self.walking_frames_right.append(image)

		image = sprite_sheet.get_image(132,93,72,90)
		self.walking_frames_right.append(image)

		image = sprite_sheet.get_image(0,186,70,90)
		self.walking_frames_right.append(image)

		#Walking Left
		sprite_sheet = SpriteSheet("p1_walk.png")
		image = sprite_sheet.get_image(0,0,66,90)
		image = pygame.transform.flip(image,True,False)
		self.walking_frames_left.append(image)

		image = sprite_sheet.get_image(66,0,66,90)
		image = pygame.transform.flip(image,True,False)
		self.walking_frames_left.append(image)

		image = sprite_sheet.get_image(132,0,67,90)
		image = pygame.transform.flip(image,True,False)
		self.walking_frames_left.append(image)


		image = sprite_sheet.get_image(0,93,66,90)
		image = pygame.transform.flip(image,True,False)
		self.walking_frames_left.append(image)

		image = sprite_sheet.get_image(66,93,66,90)
		image = pygame.transform.flip(image,True,False)
		self.walking_frames_left.append(image)

		image = sprite_sheet.get_image(132,93,72,90)
		image = pygame.transform.flip(image,True,False)
		self.walking_frames_left.append(image)

		image = sprite_sheet.get_image(0,186,70,90)
		image = pygame.transform.flip(image,True,False)
		self.walking_frames_left.append(image)

		self.image = self.walking_frames_right[0]

        # Set a reference to the image rect.
		self.rect = self.image.get_rect()


#== Draw the Player now into the surface and assign it to image
		#width = 40
		#height = 40
		#""" In the program , we already specify the width and height of the Player"""
		#self.image = pygame.Surface([width,height])
		#self.image.fill(RED)
		#self.rect = self.image.get_rect()

	def update(self):
		"""Move the Player"""
		#gravity
		self.calc_gravity()

		#Move up and Down
		self.rect.x = self.rect.x + self.change_x
		pos = self.rect.x
		if self.direction == "R":
			frame = (pos//30) % len(self.walking_frames_right)
			self.image = self.walking_frames_right[frame]
		else:
			frame = (pos //30) % len (self.walking_frames_left)
			self.image = self.walking_frames_left[frame]

	    #once we hit a wall , detect collision
		block_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
		for block in block_hit_list:
			if self.change_x > 0 :
				self.rect.right = block.rect.left
			else :
				self.rect.left = block.rect.right

		#fire_hit_list = pygame.sprite.spritecollide(self,self.level,fire_platform_list,True)
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
		self.direction="L"

	def go_right(self):
		"""Move right by 6 pxls. This is called when the user hits the right arrow"""
		self.change_x = self.change_x + 6
		self.direction = "R"

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

class invisible_wall(pygame.sprite.Sprite):

	def __init__(self,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()


class fire_Platform(pygame.sprite.Sprite):

	def __init__(self,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(YELLOW)

		self.rect = self.image.get_rect()

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

	world_shift = 0
	level_limit = -2500

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
		screen.blit(self.background,(self.world_shift // 3,0))

		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)

	def shift_world(self,shift_x):
		self.world_shift += shift_x

		for platform in self.platform_list:
			platform.rect.x += shift_x

		for enemy in self.enemy_list:
			enemy.rect.x += shift_x

class Level_01(Level):
	def  __init__(self,player):
		Level.__init__(self,player)

		self.background = pygame.image.load("./game-assets/level-backgrounds/background_01.png").convert()
		self.background.set_colorkey(WHITE)

		self.level_limit = -2500

		level=[
			   [50,30,600,100],
			   [210,50,500,500],
			   [210,50,200,400],
			   [210,50,600,300],
			   [210,50,20,120],
			   [210,50,200,200],
			   [210,50,700,400],
			   [210,50,900,500],
			   [210,50,1100,400],
			   [210,50,1600,300],
			   [210,30,2100,500]
				]

		fire_platform_list =[[210,20,2100,200]]

		invisible_wall_list = [[10,600,0,0],
								[10,600,0,-10]]

		for platform in level:
			block = Platform(platform[0],platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player #==Why do we need this
			self.platform_list.add(block)

		for platform in fire_platform_list :
			block = fire_Platform(platform[0],platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			self.platform_list.add(block)


		for platform in invisible_wall_list:
			block = invisible_wall(platform[0],platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			self.platform_list.add(block)




class Level_02(Level):
	def  __init__(self,player):
		Level.__init__(self,player)

		self.background = pygame.image.load("./game-assets/level-backgrounds/background_02.png").convert()
		self.background.set_colorkey(WHITE)

		self.level_limit = -3500

		level=[[210,30,500,500],
			   [210,30,200,400],
			   [210,30,600,300],
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
	# -- Commenting out the audio parts of the code --
	#bgm = pygame.mixer.Sound('mario.ogg')
	#bgm.play()
	screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
	pygame.display.set_caption("Platform Jumper")
    #== Create a player Object
	player = Player()

    #== Create a level list ; this will hold the levels ; right now we have only one Level
	level_list = []
	level_list.append(Level_01(player))
	level_list.append(Level_02(player))

	current_level_no = 0
	current_level = level_list[current_level_no]

    #=== Creating an Active_Sprite_List that will contain the player to start off with
	active_sprite_list = pygame.sprite.Group()
	player.level = current_level

	player.rect.x = 340
	player.rect.y = SCREEN_HEIGHT - player.rect.height
	active_sprite_list.add(player)

#== Game Loop : Step 1 : Poll for events and handle them

	done = False
#-------- Main Program Loop ---------#

	while not done:

		# -- Commenting out the audio parts of the code --
		#bgm.play()
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

#== Game Loop : Step 2 : Update the Sprites based on the above inputs

		active_sprite_list.update()
		current_level.update()

		if player.rect.right >= 500:
			diff = player.rect.right - 500
			player.rect.right = 500
			current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
		if player.rect.left <= 120:
			diff = 120 - player.rect.left
			player.rect.left = 120
			current_level.shift_world(diff)

		current_position = player.rect.x + current_level.world_shift
		if current_position < current_level.level_limit:
			player.rect.x = 120
			if current_level_no < len(level_list)-1:
				current_level_no += 1
				current_level = level_list[current_level_no]
				player.level = current_level

		if player.rect.right > SCREEN_WIDTH:
			player.rect.right = SCREEN_WIDTH

		if player.rect.left <0:
			player.rect.left = 0

#== Game Loop : Step 3 : Draw the updates sprites on the screen

		current_level.draw(screen)
		active_sprite_list.draw(screen)

#== Game Loop : Step 4 : Switch ! Flip and Display the Sprites on screen

		pygame.display.flip()

		clock.tick(60)

	pygame.quit()

if __name__ == "__main__":
	main()

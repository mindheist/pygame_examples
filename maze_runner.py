# Game Plan
# 1. Need pygame library ( import pygame)
# 2. Need some Basic colors for the Game ( Define RGB colors)
# 3. Need a basic Clock ( pygame.time.clock)
# 4. Need a Wall Class ( Use Wall Objects later on the game)
#    The Wall is a sprite and will be a subclass of the Sprite SuperClass
#    The Wall will not have any methods ,since they are static objects on the screen 
# 5. Need a Player Class ( this would be small 15 X 15 WHITE BOX )
# 5. Need a Room Class ( to go from Room to Room , changin Maze)
# 6. Need the main loop that doesnt quit till you do a pygame.event = pygame.QUIT
# 6. Need a Clock that ticks 60 times
# 7. Need a Flip Button

#=========== Step 1 as above ===============#
import pygame

#=========== Step 2 as above ===============#
#== This is based on RGB color palette =====#
BLACK  = (  0 ,   0,   0)
WHITE  = (255 , 255, 255)
RED    = (255 ,   0,   0)
GREEN  = (  0 , 255,   0)
BLUE   = (  0 ,   0, 255)
PURPLE = (255 ,   0, 255)

#=========== Step 3 as above ===============#

clock = pygame.time.Clock()
#=== This clock has to tick 60 times per min=#
#============================================#

#=========== Step 4 as above ===============#

class Wall(pygame.sprite.Sprite):
#======Step 3.1 Sub Class pygames's inbuilt Sprite Class ==#
	def __init__(self, x, y, width, height, color):
		pygame.sprite.Sprite.__init__(self)
#====== Draw a Surface & make that an image ===============#
		self.image = pygame.Surface([width,height])
		self.image.fill(color)
#===== The get_rect() function on the image treats the entire
#===== image as one rectangle and gets the x,y of the image 
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y 

#=========== Step 5 as above ===============#

class Player(pygame.sprite.Sprite):

# ==== Once again,the Player Class is also a subclass of Sprite Super Class ==#

#VARIABLES FOR THE PLAYER CLASS 

	change_x = 0
	change_y = 0

#==== Unlike the Wall Class above,Player object would not be immobile ==# 
#==== Player object would move & should be able to detect walls  ====#

	def __init__(self, x, y):
# === Define a constructor ================#
		pygame.sprite.Sprite.__init__(self)
#==== Call the Super Class's constructpr ==#
		self.image = pygame.Surface([15,15])
		self.image.fill(WHITE)
# == Draw the Player , get the x,y co-ordinates of the player ==#
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y 

#===== Player Change Speed method ====#

	def ChangeSpeed(self, x, y):
		self.change_x += x
		self.change_y += y
 # == FIND OUT,WHY THE ABOVE VARIABLE is not self.x ===#

 	def move(self, walls):
 		# Move LEFT or RIGHT
 		self.rect.x += self.change_x
 		# did the above update cause us to hit the wall ?
        # use the sprite collide to see , if the player hit the wall
		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
        		#print block
				self.rect.left = block.rect.right
        #MOVE UP OR DOWN
		self.rect.y  += self.change_y

		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		
		for block in block_hit_list:

			if  self.change_y > 0 :
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom

#===== Why do we pass Object into this class ? =====#
class Room(object):
	# Base Class for all Rooms
	# Each Room has a bunch of Walls
	# Each Room can also have enemy sprites or collectable sprites
	# which we do not use in this program

	wall_list = None
	#enemy_sprites = None

	def __init__(self):
#=== What is sprite.Group() =====================#
		self.wall_list = pygame.sprite.Group()
		#self.enemy_sprites = pygame.sprite.Group()

class Room1(Room):
	def __init__(self):
		Room.__init__(self)
#=== The following is a array of individual walls ====#
		walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE]
                ]

		for item in walls:
#=== Instantiate wall by wall and add it to the wall list =====#
			wall = Wall(item[0],item[1],item[2],item[3],item[4])
			self.wall_list.add(wall)

class Room2(Room):
	def __init__(self):
		Room.__init__(self)

		walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                ]

		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)

class Room3(Room):
    def __init__(self):
        Room.__init__(self)
 
        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)
 
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)

def main():

	pygame.init()
# Diplay Vs Screen Vs Image . Write a good few lines about the differences 
# between these

	screen = pygame.display.set_mode([800,600])

	pygame.display.set_caption('Maze Runner')

# Create a player and add it to the moving sprites list ; 
# In this particular program ; the player is the only moving component

	player = Player(50,50)
	movingsprites = pygame.sprite.Group()
	movingsprites.add(player)

# Create an Empty Room List

	rooms = [] 

	room = Room1()
	rooms.append(room)

	room = Room2()
	rooms.append(room)

	room = Room3()
	rooms.append(room)


	current_room_no = 0
	current_room = rooms[current_room_no]

#== Nothing surprising here , regular game mechanics to keep the game
#== going on till the user hits X

	done = False

	while not done:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.ChangeSpeed(-5,0)
				if event.key == pygame.K_RIGHT:
					player.ChangeSpeed(5,0)
				if event.key == pygame.K_UP:
					player.ChangeSpeed(0,-5)
				if event.key ==pygame.K_DOWN:
					player.ChangeSpeed(0,5)

# === Understand this Key-up & Why it is contradictory to KeyDown above==#
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.ChangeSpeed(5,0)
				if event.key == pygame.K_RIGHT:
					player.ChangeSpeed(-5,0)
				if event.key == pygame.K_UP:
					player.ChangeSpeed(0,5)
				if event.key ==pygame.K_DOWN:
					player.ChangeSpeed(0,-5)
		
		player.move(current_room.wall_list)
		
# == This part explains navigation between rooms and the wrapping structure ==#
 		if player.rect.x < -15:
			if current_room_no == 0:
				current_room_no = 1
				current_room = rooms[current_room_no]
				player.rect.x = 790
			elif current_room_no == 2:
				current_room_no = 1
				current_room = rooms[current_room_no]
				player.rect.x = 790
			else:
				current_room_no = 0
				current_room = rooms[current_room_no]
				player.rect.x = 790
 
		if player.rect.x > 801:
			if current_room_no == 0:
				current_room_no = 1
				current_room = rooms[current_room_no]
				player.rect.x = 0
			elif current_room_no == 1:
				current_room_no = 2
				current_room = rooms[current_room_no]
				player.rect.x = 0
			else:
				current_room_no = 0
				current_room = rooms[current_room_no]
				player.rect.x = 0

        # --- Drawing ---
		screen.fill(BLACK)
		
		movingsprites.draw(screen)
		current_room.wall_list.draw(screen)
		
		pygame.display.flip()
		
		clock.tick(60)

 	pygame.quit()
 	
if __name__ == "__main__":
    main()
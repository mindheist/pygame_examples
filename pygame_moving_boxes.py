# pygame - moving boxes
import pygame
pygame.init() 
# import and initialize pygame in the above two lines of code , Hmm .. but whats the difference though
# DEFINE COLORS FOR THE PROGRAM
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# DEFINE THE SIZE OF THE SCREEN USING VARIABLE SIZE
size = (1000,800)
# DRAW A SCREW OF THE ABOVE DIMENSION
screen = pygame.display.set_mode(size)
# WHAT ELSE IS AVAILABLE UNDER DISPLAY ? CHECK PYGAME DOCS
pygame.display.set_caption("MY GAME")

done = False
# USE THE ABOVE BOOL TO TRACK IF THE USER HAS CLICK CLOSE ; WHEN USER CLOSES THE WINDOW , THIS TURNS TRUE
clock = pygame.time.Clock()
# ABOVE CLOCK IS USED TO MANAGE HOW FREQUENTY TO UPDATE THE SCREEN
# start the main fuction of the game
rect_x = 50
rect_y = 50

rect_x_change = 5
rect_y_change = 5

while not done :
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			done = True 

	screen.fill(BLACK)
    
	pygame.draw.rect(screen,WHITE,[rect_x,rect_y,50,50])
	pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10 ,30, 30])
	rect_x = rect_x + rect_x_change
	rect_y = rect_y + rect_y_change
	if rect_x <0 or rect_x > 950:
		rect_x_change = rect_x_change * -1
	if rect_y < 0 or rect_y > 750:
		rect_y_change = rect_y_change * -1 

	pygame.display.flip()
	clock.tick(60)

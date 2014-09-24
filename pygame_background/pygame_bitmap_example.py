import pygame
import time
pygame.init()
size = (500,500)
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("basketball_ball.png").convert()
screen.blit(background_image, [0, 0])
pygame.display.flip()
time.sleep(60)






import math
import pygame
import random
# in terminal -> pip install pygame

# color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# game constants
DISPLAYWIDTH = 800
DISPLAYHEIGHT = 600
SIZE = (DISPLAYWIDTH, DISPLAYHEIGHT)
FPS = 60

##########################################################################
rect_x = 50
rect_side = 50
x_velo = 5
rect_y = 50
y_velo = 5

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pygame Picture")

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        # check for user input
        if event.type == pygame.QUIT:
            running = False

    if rect_x + rect_side > DISPLAYWIDTH or rect_x < 0:
        x_velo *= -1

    if rect_y + rect_side > DISPLAYHEIGHT or rect_y < 0:
        y_velo *= -1

    pygame.display.flip()

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, [rect_x, rect_y, rect_side, 50])
    rect_x += x_velo
    rect_y += y_velo

    clock.tick(FPS)

# quit
pygame.quit()

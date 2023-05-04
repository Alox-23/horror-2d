import pygame
from settings import *
import classes.level

pygame.init()
game = classes.level.Level()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game.run()
pygame.quit()

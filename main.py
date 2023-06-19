import pygame
from settings import *
import classes.game

pygame.init()
game = classes.game.Game()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game.run()
pygame.quit()

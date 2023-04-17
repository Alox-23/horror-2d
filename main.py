import pygame
from settings import *
from classes.level import level

pygame.init()
lev = level()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    lev.run()
pygame.quit()

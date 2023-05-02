import pygame
import sprites.player
from settings import *
import sprites.tree
import sprites.ground
import classes.objRend
import random
import classes.time
import time
import classes.level
import classes.map

class Game:
    def __init__(self):
        self.level = classes.level.Level() 

    def run(self):
        self.level.run()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.CameraGroup.scale_factor += 0.01
        if keys[pygame.K_DOWN]:
            self.CameraGroup.scale_factor -= 0.01
        if keys[pygame.K_e]:
            self.CameraGroup.set_shake_time(30)
        if keys[pygame.K_q]:
            self.CameraGroup.set_shake_time(0)


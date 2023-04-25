import pygame
import time
from settings import *

class Time:
    def __init__(self):
        self.dt = 0
        self.time = 0
        self.time_delay = 1
        self.clock = pygame.time.Clock()

    def update_time(self):
        self.dt = time.time()-self.time
        self.dt *= tFPS
        self.time = time.time()

    def update(self, delay = 1):
        self.clock.tick(FPS)
        self.update_time()
        self.delay = delay

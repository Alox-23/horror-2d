import pygame
import sprites.player
from settings import *
import sprites.tree
import sprites.ground
import classes.objRend
import random
import classes.time
import time
import classes.map

class level:
    def __init__(self):
        self.setup_level()

    def run(self):
        self.get_input()
        self.time.update()
        self.update_sprites()
        self.update_player()
        self.draw()
        pygame.display.set_caption(str(int(self.time.clock.get_fps())))
        if self.CameraGroup.screan_shake_time:
            self.CameraGroup.screan_shake(40) 
        self.CameraGroup.draw()
        pygame.display.update()

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

		
    def draw(self):
        self.CameraGroup.draw_tiles(self.tiles)
        self.CameraGroup.ysort_draw()
        for i in self.collision_rects:
            pygame.draw.rect(self.CameraGroup.display, (255, 255, 255), i)
        

    def update_sprites(self):
        self.CameraGroup.update_all(self.time.dt, self.collision_rects, self.tiles)

    def update_player(self):
        self.player.collision(self.collision_rects)
	
    def setup_level(self):
        self.time = classes.time.Time() 
        self.CameraGroup = classes.objRend.objRend()
        self.player = sprites.player.player((HRES//2,VRES//2), self.CameraGroup)
        self.CameraGroup.set_focal_point(self.player)
        self.collision_rects = [pygame.Rect(random.randint(-1500, 1500), random.randint(-1500, 1500), random.randint(1,500), random.randint(1,50)) for i in range(100)]
        self.map = classes.map.Map()
        self.map.setup_level()
        self.tiles = self.map.get_tiles()
        print(self.tiles)

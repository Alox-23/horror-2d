import pygame
import sprites.player
from settings import *
import sprites.tree
import sprites.ground
import sprites.CameraGroup
import random
import time

class level:
    def __init__(self):
        self.screan = pygame.display.set_mode((HRES, VRES))
        self.scale_factor = 1
        self.time = 0
        self.dt = 0
        self.display = pygame.Surface((HRES//self.scale_factor, VRES//self.scale_factor))
        self.clock = pygame.time.Clock()
        self.CameraGroup = sprites.CameraGroup.CameraGroup(self.display)
        self.player = sprites.player.player((HRES//2,VRES//2), self.CameraGroup)
        self.collision_rects = [pygame.Rect(random.randint(-1500, 1500), random.randint(-1500, 1500), random.randint(1,500), random.randint(1,50)) for i in range(20)]
        self.setup_level()

    def run(self):
        self.get_input()
        self.display = pygame.Surface((HRES//self.scale_factor, VRES//self.scale_factor))
        self.display.fill((50, 50, 100))
        self.update_time()
        self.update_sprites()
        self.update_player()
        self.draw()
        pygame.display.set_caption(str(int(self.clock.get_fps())))
        self.screan.blit(pygame.transform.scale(self.display, (HRES, VRES)), (0,0))
        pygame.display.update()
        self.clock.tick(FPS)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.scale_factor += 0.01
        if keys[pygame.K_DOWN]:
            self.scale_factor -= 0.01
        if keys[pygame.K_e]:
            self.CameraGroup.set_shake_time(30)
		
    def update_time(self):
        self.dt = time.time()-self.time
        self.dt *= tFPS
        self.time = time.time()
		
    def draw(self):
        self.CameraGroup.ysort_draw()
        for i in self.collision_rects:
            pygame.draw.rect(self.display, (255, 255, 255), i)

    def update_CameraGroup(self):
        self.CameraGroup.set_focal_point(self.player)
        self.CameraGroup.update_display(self.display)
        self.CameraGroup.update_scroll(self.scale_factor)
        self.CameraGroup.update_dt(self.dt)
        self.CameraGroup.update_rect_scroll(self.collision_rects)
        self.CameraGroup.update()
       

    def update_sprites(self):
        self.update_CameraGroup()

    def update_player(self):
        self.player.collision(self.collision_rects)
	
    def setup_level(self):
        for i in range(20):
            sprites.tree.tree((random.randint(-1500, 1500), random.randint(-1500, 1500)), self.CameraGroup)

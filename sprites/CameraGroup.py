import pygame
import sprites.ground
import random 
from settings import *

class CameraGroup(pygame.sprite.Group):
    def __init__(self, display):
        super().__init__()
        self.screan = display
        self.scroll = pygame.math.Vector2()
        self.delay = 20
        self.screan_shake_time = 0
        self.bg = sprites.ground.ground((HRES//2,VRES//2))
        self.add(self.bg)
        

    def update_scroll(self, scale_factor, shake_intensity = 4):
        self.scroll.x = (self.focal_point.rect.centerx-self.scroll.x-(HRES//scale_factor)//2)//self.delay
        self.scroll.y = (self.focal_point.rect.centery-self.scroll.y-(VRES//scale_factor)//2)//self.delay
        
        if self.screan_shake_time > 0:
            self.screan_shake_time -= 1

        if self.screan_shake_time:
            self.screan_shake(shake_intensity)

        for sprite in self.sprites():
            sprite.rect.centerx -= self.scroll.x
            sprite.rect.centery -= self.scroll.y

    def screan_shake(self, intensity):
        self.scroll.x -= random.randint(0,intensity)-intensity
        self.scroll.y -= random.randint(0,intensity)-intensity
        self.scroll.x += random.randint(0,intensity)-intensity
        self.scroll.y += random.randint(0,intensity)-intensity
    
    def set_shake_time(self, time):
        self.screan_shake_time = time

    def update_dt(self, dt):
        for sprite in self.sprites():
            sprite.update_dt(dt)

    def update_rect_scroll(self, rects):
        for rect in rects:
            rect.x -= self.scroll.x
            rect.y -= self.scroll.y
    
    def set_focal_point(self, obj):
        self.focal_point = obj

    def update_display(self,display):
        self.screan = display

    def ysort_draw(self):
        self.bg.draw(self.screan)
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            if type(sprite) != type(self.bg):
                sprite.draw(self.screan) 

        

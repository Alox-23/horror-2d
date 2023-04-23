import pygame
import sprites.ground
from settings import *

class CameraGroup(pygame.sprite.Group):
    def __init__(self, display):
        super().__init__()
        self.screan = display
        self.scroll = pygame.math.Vector2()
        self.delay = 20
        self.bg = sprites.ground.ground((HRES//2,VRES//2))
        self.add(self.bg)
        

    def update_scroll(self, scale_factor):
        self.scroll.x = (self.focal_point.rect.centerx-self.scroll.x-(HRES//scale_factor)//2)//self.delay
        self.scroll.y = (self.focal_point.rect.centery-self.scroll.y-(VRES//scale_factor)//2)//self.delay
        
        for sprite in self.sprites():
            sprite.rect.centerx -= self.scroll.x
            sprite.rect.centery -= self.scroll.y

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
                sprite.draw(.screan) 

        

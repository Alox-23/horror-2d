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
        

    def update_scroll(self):
        self.scroll.x = (self.focal_point.rect.centerx-self.scroll.x-HRES//2)//self.delay
        self.scroll.y = (self.focal_point.rect.centery-self.scroll.y-VRES//2)//self.delay
        
        for sprite in self.sprites():
            sprite.rect.centerx -= self.scroll.x
            sprite.rect.centery -= self.scroll.y
    
    def set_focal_point(self, obj):
        self.focal_point = obj

    def ysort_draw(self):
        self.bg.draw(self.screan)
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            if type(sprite) != type(self.bg):
                self.screan.blit(sprite.image,sprite.rect)
        

import pygame
import sprites.ground
import random 
from settings import *

class objRend(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.scale_factor = 2
        self.screan = pygame.display.set_mode((HRES, VRES))
        self.scroll = pygame.math.Vector2()
        self.delay = 20
        self.screan_shake_time = 0
        self.sprite_rects = []
        self.tiles = []
        indent = 0
        self.render_rect = pygame.Rect(0, 0, HRES//self.scale_factor-indent, VRES//self.scale_factor-indent)
        self.render_rect.center = (HRES//(self.scale_factor+2),VRES//(self.scale_factor+2))

    def update_scroll(self, shake_intensity = 4):
        self.scroll.x = (self.focal_point.rect.centerx-self.scroll.x-(HRES//self.scale_factor)//2)//self.delay
        self.scroll.y = (self.focal_point.rect.centery-self.scroll.y-(VRES//self.scale_factor)//2)//self.delay 

        for sprite in self.sprites():
            sprite.update_scroll(self.scroll.x, self.scroll.y)

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
    
    def update_all(self, dt, rects):
        self.update_display()
        self.update_scroll()
        self.update_dt(dt)
        self.update_rect_scroll(rects)
        self.update() 

    def update_display(self):
        self.render_rect.center = (HRES//(self.scale_factor+2),VRES//(self.scale_factor+2))
        self.display = pygame.Surface((HRES//self.scale_factor, VRES//self.scale_factor))

    def draw(self):
        self.screan.blit(pygame.transform.scale(self.display, (HRES, VRES)), (0,0))
            
    def ysort_draw(self):
        obj_rendered = 0
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.coll_rect.centery):
            if pygame.Rect.colliderect(sprite.rect, self.render_rect):
                sprite.draw(self.display)
                obj_rendered += 1
        print(f"Sprite objects rendered: {obj_rendered}")
        

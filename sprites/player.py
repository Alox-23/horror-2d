import pygame
from settings import *
import sprites.dummy

class player(sprites.dummy.Dummy):
    def __init__(self, pos, group):
        super().__init__(group)
        self.speed = 2
        self.dt = 1
        self.direction = pygame.math.Vector2()

        self.animations = self.load_animation(pygame.image.load("img/player/player1.png").convert_alpha(), [48, 48], 6, "idle", "idle2", "idle3", "run", "run_side", "run_up")
        self.action = "idle"
        self.animation_time = pygame.time.get_ticks()
        self.animation_index = 0
        self.flip = pygame.math.Vector2()
        self.image = self.animations[self.action][self.animation_index]

        self.y_intercept = -6
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.coll_rect = pygame.Rect(pos, (20, 21))
        self.coll_rect.center = pos 
    def update_scroll(self, dx, dy):
        self.coll_rect.centerx -= dx
        self.coll_rect.centery -= dy

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        self.direction.y = 0
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.flip.y = -1
            self.flip.x = 0
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.flip.y = 1
            self.flip.x = 0
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.flip.x = -1
            self.flip.y = 0
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.flip.x = 1
            self.flip.y = 0
    
    def update(self): 
        self.coll_rect.centerx += (self.direction.x * self.speed)*self.dt
        self.coll_rect.centery += (self.direction.y * self.speed)*self.dt
        self.update_animation(300//self.speed)
        self.input()
        self.coll_toll = (self.speed)*self.dt+self.speed
        self.rect.center = (self.coll_rect.centerx, self.coll_rect.centery+self.y_intercept)
        self.update_action()

    def update_action(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if self.flip.x == 1:
                self.action = "idle2"
                self.flip.y = 0
            elif self.flip.x == -1: 
                self.action = "idle2"
                self.flip.y = 0
            if self.flip.y == 1:
                self.action = "idle"
                self.flip.x = 0
            elif self.flip.y == -1:
                self.action = "idle3"
                self.flip.x = 0
        else:
            if self.flip.y == 1:
                self.action = "run"
            elif self.flip.y == -1:
                self.action = "run_up"
            if self.flip.x == 1:
                self.action = "run_side"
            elif self.flip.x == -1: 
                self.action = "run_side"
             
    def draw(self, screan):
        #pygame.draw.rect(screan, (255, 0, 0), self.coll_rect)
        if self.flip.x == -1:
            screan.blit(pygame.transform.flip(self.image, True, False), self.rect)
        else:
            screan.blit(self.image, self.rect) 

    def collision(self, rects): 
        for rect in rects:  
            if self.coll_rect.colliderect(rect):
                if abs(self.coll_rect.top - rect.bottom) < self.coll_toll:
                    self.coll_rect.top = rect.bottom
                elif abs(self.coll_rect.bottom - rect.top) < self.coll_toll:
                    self.coll_rect.bottom = rect.top
                elif abs(self.coll_rect.right - rect.left) < self.coll_toll:
                    self.coll_rect.right = rect.left  
                elif abs(self.coll_rect.left - rect.right) < self.coll_toll:
                    self.coll_rect.left = rect.right

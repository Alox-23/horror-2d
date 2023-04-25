import pygame
import sprites.dummy

class player(sprites.dummy.Dummy):
    def __init__(self, pos, group):
        super().__init__(group)
        self.speed = 2
        self.coll_toll = self.speed+0.1
        self.dt = 1
        self.direction = pygame.math.Vector2()

        self.animations = self.load_animation(pygame.image.load("img/player/player1.png"), [48, 48], 6, "idle", "idle2", "idle3", "run", "run_side", "run_up")
        self.action = "idle"
        self.animation_time = pygame.time.get_ticks()
        self.animation_index = 0
        self.flip = pygame.math.Vector2()

        self.rect = pygame.Rect(pos, (13, 19))

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
        self.update_animation(300//self.speed)
        self.input()
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
        if self.flip.x == -1:
            screan.blit(pygame.transform.flip(self.image, True, False), ((self.rect.x - self.image.get_width()//2)+6, self.rect.y - self.image.get_width() // 2))
        else:
            screan.blit(self.image, ((self.rect.x - self.image.get_width()//2)+6, self.rect.y - self.image.get_width() // 2))
        
    def collision(self, rects):
        self.rect.centerx += (self.direction.x * self.speed)*self.dt
        self.rect.centery += (self.direction.y * self.speed)*self.dt
        for rect in rects:   
            if self.rect.colliderect(rect):
                if abs(self.rect.top - rect.bottom) < self.coll_toll:
                    self.rect.top = rect.bottom
                    self.rect.y += 1
                elif abs(self.rect.bottom - rect.top) < self.coll_toll:
                    self.rect.bottom = rect.top
                    self.rect.y -= 1
                elif abs(self.rect.right - rect.left) < self.coll_toll:
                    self.rect.right = rect.left 
                    self.rect.x -= 1
                elif abs(self.rect.left - rect.right) < self.coll_toll:
                    self.rect.left = rect.right
                    self.rect.x += 1

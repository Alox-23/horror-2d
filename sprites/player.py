import pygame
import sprites.dummy

class player(sprites.dummy.Dummy):
    def __init__(self, pos, group):
        super().__init__(group)
        self.speed = 3
        self.coll_toll = self.speed+0.1
        self.dt = 0
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
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.flip.y = 1
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.flip.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.flip.y = 1
    
    def update(self):
        self.update_animation()
        self.input()
        self.update_action()

    def update_action(self):
        print(self.direction.x, self.direction.y, self.flip.x, self.flip.y)
        if self.direction.x == 0 and self.direction.y == 0:
            if self.flip.y == 1:
                self.action = "idle"
                print("idle")
            elif self.flip.y == -1:
                self.action = "idle3"
            elif self.flip.x == 1:
                self.action = "idle2"
            elif self.flip.x == -1: 
                self.action = "idle2"
        else:
            print("player movint")
            if self.flip.y == 1:
                self.action = "run"
            elif self.flip.y == -1:
                self.action = "run_up"
            elif self.flip.x == 1:
                self.action = "run_side"
            elif self.flip.x == -1: 
                self.action = "run_side"
             

        """elif self.flip.y == -1 and self.flip.x == 0:
            self.action = "run_up"
        elif self.flip.y == 1 and self.flip.x == 0:
            self.action = "run"
        elif self.flip.x == 1:
            self.action = "run_side"
        elif self.flip.x == -1: 
            self.action = "run_side"""

            


    def draw(self, screan):
        pygame.draw.rect(screan, (255, 0, 0),self.rect)
        screan.blit(self.image, ((self.rect.x - self.image.get_width()//2)+6, self.rect.y - self.image.get_width() // 2))
        
    def update_dt(self, dt):
        self.dt = dt
        
    def collision(self, rects):
        self.rect.centerx += self.direction.x * self.speed
        self.rect.centery += self.direction.y * self.speed
        for rect in rects:   
            if self.rect.colliderect(rect):
                if abs(self.rect.top - rect.bottom) < self.coll_toll:
                    self.rect.top = rect.bottom
                elif abs(self.rect.bottom - rect.top) < self.coll_toll:
                    self.rect.bottom = rect.top
                elif abs(self.rect.right - rect.left) < self.coll_toll:
                    self.rect.right = rect.left 
                elif abs(self.rect.left - rect.right) < self.coll_toll:
                    self.rect.left = rect.right
                """if self.direction.y > 0 and self.direction.x > 0:
                    self.rect.centerx += self.speed
                if self.direction.y < 0 and self.direction.x > 0:
                    self.rect.centery += self.speed
                if self.direction.y < 0 and self.direction.x < 0:
                    self.rect.centerx -= self.speed
                if self.direction.y > 0 and self.direction.x > 0:
                    self.rect.centery -= self.speed"""


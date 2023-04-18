import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("img/player.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.speed = 3
        self.direction = pygame.math.Vector2()

        self.rect.center = pos

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        self.direction.y = 0
        if keys[pygame.K_w]:
            self.direction.y = -1
        if keys[pygame.K_s]:
            self.direction.y = 1
        if keys[pygame.K_a]:
            self.direction.x = -1 
        if keys[pygame.K_d]:
            self.direction.x = 1
    
    def update(self):
        self.input() 

    def draw(self, screan):
        screan.blit(self.image, self.rect)

    def collision(self, rects):
        self.rect.centerx += self.direction.x * self.speed
        self.rect.centery += self.direction.y * self.speed
        for rect in rects:   
            if self.rect.colliderect(rect):
                if abs(self.rect.bottom - rect.top) < self.speed and self.direction.y > 0:
                    self.rect.centery -= self.direction.y * self.speed
                if abs(self.rect.top - rect.bottom) < self.speed and self.direction.y < 0:
                    self.rect.centery -= self.direction.y * self.speed
                if abs(self.rect.right - rect.left) < self.speed and self.direction.x < 0:
                    self.rect.centerx -= self.direction.x * self.speed
                if abs(self.rect.left - rect.right) < self.speed and self.direction.x > 0:
                    print("ahh dady")
                    self.rect.centerx -= self.direction.x * self.speed

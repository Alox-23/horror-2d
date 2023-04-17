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
        self.rect.center += self.direction * self.speed

    def draw(self, screan):
        screan.blit(self.image, self.rect)
        

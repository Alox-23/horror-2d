import pygame

class Grass1(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.img = pygame.image.load("img/tiles/square_tiles/grass.png")
        self.rect = self.img.get_rect()
        self.rect.center = pos
    
    def draw(self, screan):
        screan.blit(self.img, self.rect)

    def update(self):
        pass

import pygame

class tree:
    def __init__(self, x, y):
        self.img = pygame.image.load("img/tree.png")
        self.rect = self.img.get_rect()
        self.img.set_colorkey((255, 255, 255))
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self, screan):
        screan.blit(self.img, self.rect)

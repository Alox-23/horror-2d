import pygame

class ground:
    def __init__(self, x, y):
        self.img = pygame.image.load("img/ground.png")
        self.rect = self.img.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

    def draw(self, screan):
        screan.blit(self.img, self.rect)

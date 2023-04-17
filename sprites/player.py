import pygame

class player:
    def __init__(self, x, y):
        self.img = pygame.image.load("img/player.png")
        self.img.set_colorkey((255, 255, 255))
        self.rect = self.img.get_rect()
        self.speed = 3

        self.rect.centerx = x
        self.rect.centery = y

    def draw(self, screan):
        screan.blit(self.img, self.rect)

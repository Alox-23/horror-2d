import pygame

class ground(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load("img/ground.png")
        self.rect = self.image.get_rect()

        self.rect.center = pos

    def draw(self, screan):
        screan.blit(self.image, self.rect)

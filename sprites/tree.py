import pygame

class tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("img/tree.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.center = pos

    def draw(self, screan):
        screan.blit(self.image, self.rect)

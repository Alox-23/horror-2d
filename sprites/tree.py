import pygame
import sprites.dummy

class Tree(sprites.dummy.Dummy):
    def __init__(self, pos, _type):
        super().__init__()
        self.type = _type
        self.image = pygame.image.load("img/tree.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = pygame.Rect(pos, (35, 15))

    def update_scroll(self ,dx, dy):
        self.rect.centerx -= dx
        self.rect.centery -= dy

    def draw(self, screan):
        screan.blit(self.image, ((self.rect.x - self.image.get_width()//2)+11, self.rect.y - self.image.get_width() // 2 - 70))

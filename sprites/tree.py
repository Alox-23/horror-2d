import pygame
import sprites.dummy

class Tree(sprites.dummy.Dummy):
    def __init__(self, pos, _type):
        super().__init__()
        self.type = _type
        self.image = pygame.image.load("img/tree.png").convert()
        self.image.set_colorkey((0,0,0))
        self.coll_rect = pygame.Rect(pos, (35, 15))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.y_intercept = 60

    def update_scroll(self ,dx, dy):
        self.rect.centerx -= dx
        self.rect.centery -= dy
        self.coll_rect.center = (self.rect.centerx+5, self.rect.centery+self.y_intercept)

    def draw(self, screan):
        #pygame.draw.rect(screan, (255, 255, 255), self.rect)
        screan.blit(self.image, self.rect)
        pygame.draw.rect(screan, (255, 0, 0), self.coll_rect)

import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        super().__init__()
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.center = pos
    
    def draw(self, screan):
        screan.blit(self.img, self.rect)

    def update_scroll(self, dx, dy):
        self.rect.centerx -= dx
        self.rect.centery -= dy

import pygame

class lightCircle:
    def __init__(self, radius, color, size, x, y, light_scale = 2):
        self.rad = radius
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.img = pygame.Surface((radius * 2 + 0.1, radius * 2+ 0.1))
        pygame.draw.circle(self.img, color, (radius, radius), radius)
        self.img.set_colorkey((0, 0, 0))
		
    def update(self, x, y, change = 0):
        self.size -= change
        self.rect.x = x-self.size//2
        self.rect.y = y-self.size//2
        print(self.rect.x, self.rect.y)
		
    def draw(self,screan):
        screan.blit(pygame.transform.scale(self.img, (self.size, self.size)), self.rect, special_flags = pygame.BLEND_RGB_ADD)
		

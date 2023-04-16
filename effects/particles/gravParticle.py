import pygame
from particles.Particle import Particle

class gravParticle(Particle):
    def update(self, change, rand, rects, b, delta_time):
        self.change = change
        self.dy += self.gravity
        self.size -= change
        self.rect = pygame.Rect(self.x, self.y, self.size*2, self.size*2)

        self.x += self.dx * delta_time
        self.y += self.dy * delta_time
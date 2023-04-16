import pygame
from effects.particles.gravParticle import gravParticle
import math
import effects.particles.light as light


class pycParticle(gravParticle):

    def __init__(self,
                 x,
                 y,
                 span,
                 size,
                 dx,
                 dy,
                 g,
                 light_type=light.lightCircle,
                 light_radius=5,
                 light_color=(50, 50, 50),
				 light_mask = 0,
				 light_size = (10, 10),
				 colorkey = (0,0,0)):
        super().__init__(x,
                         y,
                         span,
                         size,
                         dx,
                         dy,
                         g,
                         light_type=light_type,
                         light_radius=light_radius,
                         light_color=light_color,
						 light_mask=light_mask,
						 light_size = light_size,
					     colorkey = colorkey)
        print(light_size)
        self.br = -2

    def Collide(self, rects, b):
        for rect in rects:
            if self.br < 0:
                self.horCollide(rect, b)
            else:
                self.vertCollide(rect, b)

    def vertCollide(self, rect, b):
        if pygame.Rect.colliderect(self.rect, rect):
            self.dy = self.dy * -b

    def horCollide(self, rect, b):
        if pygame.Rect.colliderect(self.rect, rect):
            self.dx = self.dx * -b

    def update(self, change, rand, rects, b, delta_time):
        self.change = change
        self.dy += self.gravity
        self.size -= change
        self.rect = pygame.Rect(self.x, self.y, self.size * 2, self.size * 2)

        self.Collide(rects, b)
        self.x += self.dx * delta_time
        self.y += self.dy * delta_time
        self.br *= -1

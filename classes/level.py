import pygame
import sprites.player
from settings import *
import sprites.tree
import sprites.ground
import random

class level:
    def __init__(self):
        self.screan = pygame.display.set_mode((HRES, VRES))
        self.display = pygame.Surface((HRES, VRES))
        self.clock = pygame.time.Clock()
        self.sprites = []
        self.bg = sprites.ground.ground(HRES//2, VRES//2)
        self.player = sprites.player.player(HRES//2,VRES//2)
        self.setup_level()

    def run(self):
        self.get_input()
        self.display.fill((50, 50, 100))
        self.draw()
        self.screan.blit(pygame.transform.scale(self.display, (HRES, VRES)), (0,0))
        pygame.display.update()
        self.clock.tick(FPS)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.player.rect.centery -= self.player.speed
        if keys[pygame.K_s]:
            self.player.rect.centery += self.player.speed
        if keys[pygame.K_a]:
            self.player.rect.centerx -= self.player.speed
        if keys[pygame.K_d]:
            self.player.rect.centerx += self.player.speed

        if keys[pygame.K_r]:
            self.sprites = []
            self.setup_level()

    def draw(self):
        self.bg.draw(self.display)
        self.player.draw(self.display)
        self.draw_sprites()

    def setup_level(self):
        for i in range(10):
            self.sprites.append(sprites.tree.tree(random.randint(-1500, 1500), random.randint(-1500, 1500)))

    def draw_sprites(self):
        for sprite in self.sprites:
            sprite.draw(self.display)

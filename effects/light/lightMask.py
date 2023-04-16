import pygame
from light.lightCircle import lightCircle

class lightMask(lightCircle):
	def __init__(self, mask, x, y, size = 10, colorkey = (0,0,0)):
		self.img = mask
		self.size = size
		self.img = pygame.transform.scale(self.img, (size, size))
		self.img.set_colorkey(colorkey)
		self.rect = self.img.get_rect()
		self.rect.x = x
		self.rect.y = y
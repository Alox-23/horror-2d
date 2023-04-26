import pygame

class Dummy(pygame.sprite.Sprite):
    def init(self, group):
        super().__init__(group)

    def load_animation(self, sheet, size, items, *animation_types):
        animations = {}
        for row in range(len(animation_types)):
            animation_list = []
            y = row*size[1]
            for img in range(items):
                x = img*size[0]
                animation_list.append(sheet.subsurface(x, y, size[0], size[1]))

            animations[animation_types[row]] = animation_list

        return animations
            
    def update_dt(self, dt):
        self.dt = dt
        
    def update_animation(self, cool=200):
        self.ANIMATION_COOLDOWN = cool
        self.image = self.animations[self.action][self.animation_index]
        if pygame.time.get_ticks() - self.animation_time > self.ANIMATION_COOLDOWN:
            self.animation_index += 1
            self.animation_time = pygame.time.get_ticks()
        if self.animation_index > len(self.animations[self.action])-1:
            self.animation_index = 0

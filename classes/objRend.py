import pygame

class objRend:
    def __init__(self):
        self.obj_to_render = []

    def add_obj(self, obj):
        self.obj_to_render.append(obj)

    def draw_obj(self, shift_x = 0, shift_y = 0):
        for obj in self.obj_to_render:
            if len(obj.vars[-1]) == 0:
                 obj.vars[0].blit(obj.vars[1], (obj.vars[2], obj.vars[3]))
            else:
                 obj.vars[0].blit(obj.vars[1], (obj.vars[2], obj.vars[3]), special_flags = obj.[-1])

class obj:
    def __init__(self, screan, surf, x, y, flags = []):
        self.vars = [screan, surf, x, y, flags]

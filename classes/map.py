import pygame
import random
import sprites.tiles.grass
import sprites.tiles.grass1

class Map:
    def __init__(self):
        self.setup_level()
        
    def setup_level(self):
        self.tiles = [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

                ]
        self.plant_dat = [[(random.randint(0, len(self.tiles[0])*32), random.randint(0, len(self.tiles)*32)),"plain"] for i in range(100)]
        self.create_tile_dat()

    def get_tiles(self):
        tiles = []
        for row in self.tile_dat:
            for tile in row:
                if tile[1] == 1:
                    tiles.append(sprites.tiles.grass.Grass(tile[0]))

                elif tile[1] == 0:
                    tiles.append(sprites.tiles.grass1.Grass1(tile[0]))
    
    def create_tile_dat(self):
        self.tile_dat = []
        for num, row in enumerate(self.tiles):
            y = num * 32
            temp_row = []
            for index, tile in enumerate(row):
                x = index * 32
                temp_row.append([(x,y), tile])
            self.tile_dat.append(sorted(temp_row, key=lambda i: i[1]))

import pygame
import random

class Map:
    def __init__(self):
        self.level_dat = {}
        self.tiles = [
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

                ]
        self.plant_dat = [[(random.randint(0, len(self.tiles[0])*32), random.randint(0, len(self.tiles)*32)),"plain"] for i in range(100)]

    def create_dat(self):
        dat = []
        for num, row in enumerate(self.tiles):
            y = num * 32
            temp_row = []
            for index, tile in enumerate(row):
               
                x = index * 32
                temp_row.append([(x,y), tile])
            dat.append(temp_row)
        for row in dat:
            for i in row:
                for j in sorted(row, key = lambda row : i[1]):
                print(j[1], end = "")
            print()

m = Map()
m.create_dat()

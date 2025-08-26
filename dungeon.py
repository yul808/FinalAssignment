import pygame

class Dungeon:
    def __init__(self, tile_size=16, map_file="map.txt"): # map.txt contains map layout
        self.tile_size = tile_size
        self.map_data = self.load_map(map_file)

    def load_map(self, filename):
        map_data = []
        with open(filename, "r") as f:
            for line in f:
                # remove spaces
                line = line.strip()
                # turn characters into int
                row = [int(char) for char in line]
                map_data.append(row)
        return map_data


    def draw(self, surface):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                rect = pygame.Rect(x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size)
                if tile == 1:
                    pygame.draw.rect(surface, (100, 100, 100), rect)  # wall
                else:
                    pygame.draw.rect(surface, (0, 0, 0), rect)  # floor

    def is_wall(self, tile_x, tile_y):
        if 0 <= tile_y < len(self.map_data) and 0 <= tile_x < len(self.map_data[0]):
            return self.map_data[tile_y][tile_x] == 1
        return True #collision detection
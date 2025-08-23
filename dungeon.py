import pygame

class Dungeon:
    def __init__(self, tile_size=16, map_file="map.txt"):
        self.tile_size = tile_size
        self.map_data = self.load_map(map_file)

    def load_map(self, filename):
        map_data = []
        with open(filename, "r") as f:
            for line in f:
                # Leerzeichen/Zeilenumbruch entfernen
                line = line.strip()
                # Jeden Character (z. B. "1" oder "0") in int umwandeln
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
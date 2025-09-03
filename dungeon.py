import pygame

class Dungeon:
    def __init__(self, tile_size=16, map_file="map.txt"): # map.txt contains map layout
        self.tile_size = tile_size
        self.map_data = self.load_map(map_file)

        self.floor_image = pygame.image.load("media/floor.png").convert()
        self.floor_image = pygame.transform.scale(self.floor_image, (990, 670))
        # Create a dark overlay
        dark_overlay = pygame.Surface(self.floor_image.get_size())
        dark_overlay.set_alpha(100)  # 0 = no darkening, 255 = completely black
        dark_overlay.fill((0, 0, 0))

        self.floor_image.blit(dark_overlay, (0, 0))

        self.wall_image = pygame.image.load("media/wall.png").convert_alpha()
        self.wall_image = pygame.transform.scale(self.wall_image, (self.tile_size, self.tile_size))

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
        surface.blit(self.floor_image, (0, 0))

        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                pos = (x * self.tile_size, y * self.tile_size)
                if tile == 1:
                    surface.blit(self.wall_image, pos)  # wall

    def is_wall(self, tile_x, tile_y):
        if 0 <= tile_y < len(self.map_data) and 0 <= tile_x < len(self.map_data[0]):
            return self.map_data[tile_y][tile_x] == 1
        return True #collision detection
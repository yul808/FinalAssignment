import pygame

class Key:
    def __init__(self, x, y, size=20):
        self.x = x
        self.y = y
        self.size = size
        self.collected = False

        self.image = pygame.image.load("media/keys.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)


    def draw(self, surface):
        if not self.collected:
            surface.blit(self.image, (self.x, self.y))
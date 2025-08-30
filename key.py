import pygame

class Key:
    def __init__(self, x, y, size=20, color=(255, 215, 0)):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.collected = False

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, surface):
        if not self.collected:
            rect = pygame.Rect(self.x, self.y, self.size, self.size)
            pygame.draw.rect(surface, self.color, rect)
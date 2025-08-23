import pygame

class Player:
    def __init__(self, x, y, size=32, color=(0, 200, 0)):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = 4

    def handle_input(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(surface, self.color, rect)
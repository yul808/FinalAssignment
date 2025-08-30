import pygame
import math #math library suggested by AI

class Enemy:
    def __init__(self, x, y, size=32, color=(200, 0, 0)):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = 1.5

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self, player):
        # calculating direction towards player
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.hypot(dx, dy) #distance between enemy and player

        if distance > 0:  #normalizing to make enemies move with constant speed; solution to a previous problem presented by AI
            dx /= distance
            dy /= distance

            #move towards player (with constant speed)
            self.x += dx * self.speed
            self.y += dy * self.speed

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(surface, self.color, rect)
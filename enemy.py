import pygame
import random
import math #math library suggested by AI

class Enemy:
    def __init__(self, x, y, size=40):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 1.5

        self.image = pygame.image.load("media/enemies.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

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

        if random.randint(0, 60) == 0:
            r = random.randint(50, 255)
            g = random.randint(50, 255)
            b = random.randint(50, 255)
            self.image = pygame.image.load("media/enemies.png").convert_alpha()
            self.image.fill((r, g, b), special_flags=pygame.BLEND_RGBA_MULT)
            self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
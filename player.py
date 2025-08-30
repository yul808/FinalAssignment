import pygame

class Player:
    def __init__(self, x, y, size=32, color=(0, 200, 0)):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = 4
    # defining player

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def can_move(self, new_x, new_y, dungeon): #helping method for collision
        rect = pygame.Rect(new_x, new_y, self.size, self.size)
        # checking all corners of player hit box
        corners = [
            (rect.left // dungeon.tile_size, rect.top // dungeon.tile_size),
            (rect.right // dungeon.tile_size, rect.top // dungeon.tile_size),
            (rect.left // dungeon.tile_size, rect.bottom // dungeon.tile_size),
            (rect.right // dungeon.tile_size, rect.bottom // dungeon.tile_size),
        ]
        for (tx, ty) in corners:
            if dungeon.is_wall(tx, ty):
                return False
        return True

    def handle_input(self, keys, dungeon):
        new_x, new_y = self.x, self.y

        if keys[pygame.K_UP]:
            new_y -= self.speed
        if keys[pygame.K_DOWN]:
            new_y += self.speed
        if keys[pygame.K_LEFT]:
            new_x -= self.speed
        if keys[pygame.K_RIGHT]:
            new_x += self.speed

        if self.can_move(new_x, new_y, dungeon):
            self.x, self.y = new_x, new_y

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(surface, self.color, rect)

    def check_collision(self, enemies): #check collision with enemy
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                return True
        return False


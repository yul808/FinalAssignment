import pygame
from dungeon import Dungeon
from player import Player

pygame.init()
display = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

dungeon = Dungeon()
player = Player(50, 50)  # starting position

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.handle_input(keys)

    display.fill((0,0,0))
    dungeon.draw(display)
    player.draw(display)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
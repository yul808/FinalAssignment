# DISCLAIMER
# AI was used throughout this project for finding fitting approaches
# as well as a mean of consultation regarding coding habits and conventions.
# It was also used to analyse errors within the code.

import pygame
from dungeon import Dungeon #importing map
from player import Player #importing player

pygame.init()
display = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

dungeon = Dungeon()
player = Player(50, 50)  # player starting position

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.handle_input(keys, dungeon)

    display.fill((0,0,0))
    dungeon.draw(display)
    player.draw(display)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
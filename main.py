# DISCLAIMER
# AI was used throughout this project for finding fitting approaches
# as well as a mean of consultation regarding coding habits and conventions.
# It was also used to analyse errors with the code.

import pygame
from dungeon import Dungeon #importing map
from player import Player #importing player
from enemy import Enemy #importing enemies


pygame.init()
display = pygame.display.set_mode((1200, 700)) #setting display
pygame.display.set_caption("HAUNTED HOUSE") #game title in window
clock = pygame.time.Clock()

dungeon = Dungeon()
player = Player(50, 50)  # player starting position
enemies = [
    Enemy(400, 400),
    Enemy(800, 200),
    Enemy(600, 300),
    Enemy(60, 400)
] #enemies starting positions

running = True # Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    player.handle_input(keys, dungeon) #player input for movement (player.py)

    for enemy in enemies:
        enemy.update(player)  # update enemies according to player position (enemy.py)

    display.fill((0,0,0))
    dungeon.draw(display) #drawing map (dungeon.py)
    player.draw(display) #drawing player (player.py)

    for enemy in enemies:
        enemy.draw(display) #drawing enemies (enemy.py)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
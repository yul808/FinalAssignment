# DISCLAIMER
# AI was used throughout this project for finding fitting approaches
# as well as a mean of consultation regarding coding habits and conventions.
# It was also used to analyse errors with the code.

import pygame
from dungeon import Dungeon
from player import Player
from enemy import Enemy

pygame.init()
display = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("HAUNTED HOUSE")
clock = pygame.time.Clock()

#Game setup function
def new_game():
    dungeon = Dungeon()
    player = Player(50, 50)
    enemies = [
        Enemy(400, 400),
        Enemy(800, 200),
        Enemy(600, 300),
        Enemy(60, 400)
    ]
    return dungeon, player, enemies

dungeon, player, enemies = new_game()

running = True
game_over = False

font = pygame.font.SysFont("consolas", 40)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        # Normal gameplay
        player.handle_input(keys, dungeon)

        for enemy in enemies:
            enemy.update(player)

        # Check for death
        if player.check_collision(enemies):
            game_over = True

        # Draw
        display.fill((0, 0, 0))
        dungeon.draw(display)
        player.draw(display)
        for enemy in enemies:
            enemy.draw(display)

    else:
        # Game Over screen
        display.fill((0, 0, 0))
        text = font.render("GAME OVER - Press SPACE to restart", True, (200, 0, 0))
        display.blit(text, (200, 300))

        if keys[pygame.K_SPACE]:
            dungeon, player, enemies = new_game()
            game_over = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
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

# Game setup function (so we can reset easily)
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
game_state = "start"  #possible game states: "start", "playing", "game_over"

font_big = pygame.font.SysFont("consolas", 72)
font_small = pygame.font.SysFont("consolas", 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_state == "start":
        # START SCREEN
        display.fill((0, 0, 0))
        title = font_big.render("HAUNTED HOUSE", True, (200, 0, 0))
        prompt = font_small.render("Press SPACE to start", True, (255, 255, 255))
        display.blit(title, (350, 250))
        display.blit(prompt, (420, 400))

        if keys[pygame.K_SPACE]:
            dungeon, player, enemies = new_game()
            game_state = "playing"

    elif game_state == "playing":
        # GAMEPLAY
        player.handle_input(keys, dungeon)

        for enemy in enemies:
            enemy.update(player)

        # Check for death
        if player.check_collision(enemies):
            game_state = "game_over"

        # Draw world
        display.fill((0, 0, 0))
        dungeon.draw(display)
        player.draw(display)
        for enemy in enemies:
            enemy.draw(display)

    elif game_state == "game_over":
        # GAME OVER SCREEN
        display.fill((0, 0, 0))
        text = font_big.render("GAME OVER", True, (200, 0, 0))
        prompt = font_small.render("Press SPACE to restart", True, (255, 255, 255))
        display.blit(text, (430, 250))
        display.blit(prompt, (420, 400))

        if keys[pygame.K_SPACE]:
            dungeon, player, enemies = new_game()
            game_state = "playing"

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
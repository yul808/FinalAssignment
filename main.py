# DISCLAIMER
# AI was used throughout this project for finding fitting approaches
# as well as a mean of consultation regarding coding habits and conventions.
# It was also used to analyse errors with the code.

import pygame
from dungeon import Dungeon
from player import Player
from enemy import Enemy
from key import Key

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
    keys = [
        Key(250, 100),
        Key(900, 150),
        Key(500, 500),
        Key(300, 300),
        Key(950, 600),
    ]
    return dungeon, player, enemies, keys

dungeon, player, enemies, keys = new_game()

running = True
game_state = "start"  #possible game states: "start", "playing", "game_over", "win"

font_big = pygame.font.SysFont("consolas", 72)
font_small = pygame.font.SysFont("consolas", 36)

# Exit zone rectangle (bottom left corner)
exit_zone = pygame.Rect(50, 600, 80, 80)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    if game_state == "start":
        display.fill((0, 0, 0))
        title = font_big.render("HAUNTED HOUSE", True, (200, 0, 0))
        prompt = font_small.render("Press SPACE to start", True, (255, 255, 255))
        display.blit(title, (350, 250))
        display.blit(prompt, (420, 400))

        if keys_pressed[pygame.K_SPACE]:
            dungeon, player, enemies, keys = new_game()
            game_state = "playing"

    elif game_state == "playing":
        # GAMEPLAY
        player.handle_input(keys_pressed, dungeon)

        for enemy in enemies:
            enemy.update(player)

        # Enemy collision = death
        if player.check_collision(enemies):
            game_state = "game_over"

        # Key collection
        for key in keys:
            player.collect_key(key)

        # Check win condition
        if player.keys_collected == 5 and player.rect.colliderect(exit_zone):
            game_state = "win"

        # Draw world
        display.fill((0, 0, 0))
        dungeon.draw(display)

        # Draw keys
        for key in keys:
            key.draw(display)

        # Draw exit zone
        pygame.draw.rect(display, (0, 0, 200), exit_zone)

        # Draw player and enemies
        player.draw(display)
        for enemy in enemies:
            enemy.draw(display)

        # Show collected keys
        text = font_small.render(f"Keys: {player.keys_collected}/5", True, (255, 255, 0))
        display.blit(text, (20, 20))

    elif game_state == "game_over":
        display.fill((0, 0, 0))
        text = font_big.render("GAME OVER", True, (200, 0, 0))
        prompt = font_small.render("Press SPACE to restart", True, (255, 255, 255))
        display.blit(text, (430, 250))
        display.blit(prompt, (420, 400))

        if keys_pressed[pygame.K_SPACE]:
            dungeon, player, enemies, keys = new_game()
            game_state = "playing"

    elif game_state == "win":
        display.fill((0, 0, 0))
        text = font_big.render("YOU ESCAPED!", True, (0, 200, 0))
        prompt = font_small.render("Press SPACE to play again", True, (255, 255, 255))
        display.blit(text, (400, 250))
        display.blit(prompt, (380, 400))

        if keys_pressed[pygame.K_SPACE]:
            dungeon, player, enemies, keys = new_game()
            game_state = "playing"

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
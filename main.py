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

# helper function for later use
def load_best_times(filename="times.txt"):
    times = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                # Split into time part and optional tag (with help from AI for this step)
                parts = line.split(" ", 1)
                time_part = parts[0]
                tag = " " + parts[1] if len(parts) > 1 else ""

                try:
                    # parse "M:SS.mmm" into total milliseconds for sorting
                    minutes, rest = time_part.split(":", 1)
                    seconds, millis = rest.split(".", 1)
                    total_ms = int(minutes) * 60000 + int(seconds) * 1000 + int(millis)

                    times.append((total_ms, time_part + tag))
                except ValueError:
                    continue
    except FileNotFoundError:
        pass

    # Sort by total milliseconds, return the 5 best (help from AI)
    times.sort(key=lambda t: t[0])
    return [t[1] for t in times[:5]]

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

start_time = 0
final_time = None

# Exit zone rectangle (bottom left corner)
exit_zone = pygame.Rect(50, 575, 80, 80)

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

        best_scores = load_best_times()
        y = 500
        for score in best_scores:
            score_text = font_small.render(score, True, (200, 200, 200))
            display.blit(score_text, (480, y))
            y += 40

        if keys_pressed[pygame.K_SPACE]:
            dungeon, player, enemies, keys = new_game()
            start_time = pygame.time.get_ticks()
            final_time = None
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
            final_time = time_str
            game_state = "win"

            # Save time to file
            with open("times.txt", "a") as f:
                f.write(final_time + "\n")

        # timer code 1/2; in format 1:23.456 (a lot of help from AI; initial prompt: "This is my current code for a timer for a small game. I would prefer the timer to count tens, hundreds and thousands of a second as well. That means the times should look like this: 1:23.456 (meaning 1 minute, 23.456 seconds). What would I have to change?")
        elapsed_ms = pygame.time.get_ticks() - start_time

        minutes = elapsed_ms // 60000
        seconds = (elapsed_ms % 60000) // 1000
        milliseconds = elapsed_ms % 1000

        time_str = f"{minutes}:{seconds:02}.{milliseconds:03}"
        # :02 ensures seconds always show two digits
        # :03 ensures milliseconds always show three digits

        # Draw world
        display.fill((0, 0, 0))
        dungeon.draw(display)

        # Draw keys
        for key in keys:
            key.draw(display)

        # timer code 2/2
        elapsed_ms = pygame.time.get_ticks() - start_time
        minutes = elapsed_ms // 60000
        seconds = (elapsed_ms % 60000) // 1000
        milliseconds = elapsed_ms % 1000
        time_str = f"{minutes}:{seconds:02}.{milliseconds:03}"

        time_text = font_small.render(f"{time_str}", True, (255, 255, 255))
        display.blit(time_text, (1000, 20))

        # Draw exit zone
        pygame.draw.rect(display, (0, 0, 200), exit_zone)

        # Draw player and enemies
        player.draw(display)
        for enemy in enemies:
            enemy.draw(display)

        # Show collected keys
        text = font_small.render(f"Keys {player.keys_collected}/5", True, (255, 255, 0))
        display.blit(text, (20, 20))

    elif game_state == "game_over":
        display.fill((0, 0, 0))
        text = font_big.render("GAME OVER", True, (200, 0, 0))
        prompt = font_small.render("Press SPACE to restart", True, (255, 255, 255))
        display.blit(text, (430, 250))
        display.blit(prompt, (420, 400))

        best_scores = load_best_times()
        y = 500
        for score in best_scores:
            score_text = font_small.render(score, True, (200, 200, 200))
            display.blit(score_text, (480, y))
            y += 40

        if keys_pressed[pygame.K_SPACE]:
            dungeon, player, enemies, keys = new_game()
            start_time = pygame.time.get_ticks()
            final_time = None
            game_state = "playing"

    elif game_state == "win":
        display.fill((0, 0, 0))
        text = font_big.render("YOU ESCAPED!", True, (0, 200, 0))

        if final_time is not None:
            time_text = font_small.render(f"Your Time: {final_time}", True, (255, 255, 255))
            display.blit(time_text, (460, 350))

        prompt = font_small.render("Press SPACE to play again", True, (255, 255, 255))
        display.blit(text, (400, 250))
        display.blit(prompt, (380, 400))

        best_scores = load_best_times()
        y = 500
        for score in best_scores:
            score_text = font_small.render(score, True, (200, 200, 200))
            display.blit(score_text, (480, y))
            y += 40

        if keys_pressed[pygame.K_SPACE]:
            dungeon, player, enemies, keys = new_game()
            start_time = pygame.time.get_ticks()
            final_time = None
            game_state = "playing"

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
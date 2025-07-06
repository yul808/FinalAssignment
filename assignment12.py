import pygame

pygame.init()

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Caution: Avoid the red zones!")

red_zones = [
    pygame.Rect(300, 200, 300, 300),
    pygame.Rect(200, 100, 300, 300),
    pygame.Rect(0, 0, 80, 300),
    pygame.Rect(0, 450, 90, 300),
]

png1_raw = pygame.image.load("pixel_art.png").convert_alpha()
png2_raw = pygame.image.load("pixel_art-2.png").convert_alpha()
png1 = pygame.transform.scale(png1_raw, (100, 80))
png2 = pygame.transform.scale(png2_raw, (100, 80))

cursor_rect = png1.get_rect()

pygame.mouse.set_visible(False)

main_surface = pygame.Surface((500, 500))

run = True
while run:
    main_surface.fill("white")

    for zone in red_zones:
        pygame.draw.rect(main_surface, (50, 10, 10), zone)

    mouse_pos = pygame.mouse.get_pos()
    cursor_rect.center = mouse_pos

    over_red = any(cursor_rect.colliderect(zone) for zone in red_zones)

    if over_red:
        main_surface.blit(png2, cursor_rect.topleft)
    else:
        main_surface.blit(png1, cursor_rect.topleft)

    display.blit(main_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
# The .png is slightly bigger than the printed image shows. Therefore, there might be contact with red zones even though it is not shown visually. The issue is noted, a solution has not been found yet.

# Disclaimer: AI was used to put the bits of code in the right place so that they would execute at the correct moment in time.
import pygame

pygame.init()

if pygame.get_init():
    print("Pygame initialized successfully.")
else:
    print("Error initializing Pygame.")

pygame.display.set_caption("Heroglobine")
screen = pygame.display.set_mode((500, 800))

# assets "welcome" screen
bg_wel = pygame.image.load("assets/bg_wel.jpg")
title_wel = pygame.image.load("assets/title_wel.png")
title_wel_rect = title_wel.get_rect(center=(520, 500))
title_wel_image = pygame.transform.scale(title_wel, (500, 150))

play_btn = pygame.image.load("assets/play_btn.png")
play_btn_rect = play_btn.get_rect(center=(250, 550))

# assets "choose character" screen
choose_charac_sprite = pygame.image.load("assets/choose_character.png")
choose_charac = pygame.transform.scale(choose_charac_sprite, (485, 300))
player_sprite = pygame.image.load("assets/player.png")
player_sprite_rect = player_sprite.get_rect(center=(250, 510))

# assets "game" screen
player_sprite_rect_two = player_sprite.get_rect(center=(50, 510))


# Texte
font_size = 30
font = pygame.font.Font(None, font_size)
text_color = (0, 0, 0)
text = "a toi mon reuf !"
text_render = font.render(text, True, text_color)
text_render_rect = text_render.get_rect(center=(90, 400))

white = (255, 255, 255)
screen_state = 'welcome_screen'
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if screen_state == 'welcome_screen' and play_btn_rect.collidepoint(event.pos):
                screen_state = 'character_screen'
                screen.fill((255, 255, 255))
            elif screen_state == 'character_screen' and player_sprite_rect.collidepoint(event.pos):
                screen_state = 'game_screen'
                screen.fill((255, 255, 255))

    if screen_state == 'welcome_screen':
        screen.blit(bg_wel, (0, 0))
        screen.blit(play_btn, play_btn_rect)
        screen.blit(title_wel_image, title_wel_rect)
    elif screen_state == 'character_screen':
        screen.blit(text_render, text_render_rect)
        screen.blit(choose_charac, (0, 0))
        screen.blit(player_sprite, player_sprite_rect)
    elif screen_state == 'game_screen':
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player_sprite_rect_two.x += 0.7
        elif keys[pygame.K_LEFT]:
            player_sprite_rect_two.x -= 0.7
        screen.fill((255, 255, 255))
        screen.blit(bg_wel, (0, 0))
        screen.blit(player_sprite, player_sprite_rect_two)

    # mettre à jour la fenetre
    pygame.display.flip()

pygame.quit()

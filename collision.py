import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Player sprite
player_size = 50
player_x = 100
player_y = 250
player_speed = 1

# Target sprite (triggers "win")
target_size = 50
target_x = 650
target_y = 250

# Font for messages
font = pygame.font.Font(None, 74)  # None uses default font, 74 is size

game_over = False
win_message = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Keep player on screen
        player_x = max(0, min(player_x, SCREEN_WIDTH - player_size))
        player_y = max(0, min(player_y, SCREEN_HEIGHT - player_size))

        # Create rect objects for collision detection
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        target_rect = pygame.Rect(target_x, target_y, target_size, target_size)

        # Collision detection
        if player_rect.colliderect(target_rect):
            win_message = True
            game_over = True  # End the game after collision

    # Drawing
    screen.fill(BLUE)  # Fill background

    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))  # Draw player
    pygame.draw.rect(screen, GREEN, (target_x, target_y, target_size, target_size))  # Draw target

    if win_message:
        text_surface = font.render("YOU WIN!", True, WHITE)  # Render text (text, antialias, color)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)  # Draw text on screen

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Anime Game")

# Player settings
player_x = 370
player_y = 480
player_speed = 0.3
player_width = 50
player_height = 50
player_color = (255, 0, 0)  # Red

# Enemy settings
enemy_x = 200
enemy_y = 50
enemy_speed = 0.2
enemy_width = 50
enemy_height = 50
enemy_color = (0, 255, 0)  # Green

# --- New: Collision Detection Function ---
def is_collision(player_x, player_y, enemy_x, enemy_y, player_size, enemy_size):
    # Calculate the center points of the player and enemy
    player_center_x = player_x + player_size / 2
    player_center_y = player_y + player_size / 2
    enemy_center_x = enemy_x + enemy_size / 2
    enemy_center_y = enemy_y + enemy_size / 2

    # Calculate the distance between the centers
    distance = ((player_center_x - enemy_center_x) ** 2 + (player_center_y - enemy_center_y) ** 2) ** 0.5

    # A simple way to check collision for squares/circles is if distance is less than sum of half sizes
    # For two 50x50 squares, a distance of less than 50 means they are overlapping
    return distance < (player_size / 2 + enemy_size / 2)
    # Alternatively, for rectangles, you can use pygame.Rect.colliderect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Moving the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player within screen bounds
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width

    # Moving the enemy
    enemy_x += enemy_speed
    if enemy_x >= screen_width - enemy_width or enemy_x <= 0:
        enemy_speed *= -1

    # --- New: Check for collision ---
    if is_collision(player_x, player_y, enemy_x, enemy_y, player_width, enemy_width):
        print("Game Over!")
        running = False  # End the game if collision occurs

    # Fill the screen with background color
    screen.fill((0, 0, 255))  # Blue background

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # Draw the enemy
    pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, enemy_width, enemy_height))

    pygame.display.update()

pygame.quit()
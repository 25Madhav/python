import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("COLLECT THE COINS TO WIN!")

# Player settings
player_x = 370
player_y = 480                                
player_speed = 0.3
player_width = 50
player_height = 50
player_color = (255, 0, 0)  # Red

# --- Updated: Enemy settings for two enemies ---
# Enemy 1 settings
enemy1_x = 200
enemy1_y = 50
enemy1_speed = 0.4
enemy1_width = 50
enemy1_height = 50
enemy1_color = (0, 255, 0)  # Green

# Enemy 2 settings (new enemy)
enemy2_x = 600  # Different starting X position
enemy2_y = 150  # Different starting Y position
enemy2_speed = 0.5  # Slightly different speed
enemy2_width = 50
enemy2_height = 50
enemy2_color = (255, 165, 0)  # Orange color

# Game Variables
score = 0
lives = 3

# Font for displaying score and lives
font = pygame.font.Font(None, 36)

# Coin settings
coin_width = 30
coin_height = 30
coin_color = (255, 223, 0)  # yellow
coin_value = 1000

coin_x = random.randint(0, screen_width - coin_width)
coin_y = random.randint(100, screen_height - 200)
coin_active = True

# Coin respawn timer variables
respawn_timer_start = 0
respawn_delay = 5000  # 5 seconds in milliseconds

def is_collision(obj1_x, obj1_y, obj2_x, obj2_y, obj1_size, obj2_size):
    obj1_center_x = obj1_x + obj1_size / 2
    obj1_center_y = obj1_y + obj1_size / 2
    obj2_center_x = obj2_x + obj2_size / 2
    obj2_center_y = obj2_y + obj2_size / 2
    distance = ((obj1_center_x - obj2_center_x) ** 2 + (obj1_center_y - obj2_center_y) ** 2) ** 0.5
    return distance < (obj1_size / 2 + obj2_size / 2)

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
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed

    # Keep player within screen bounds
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width
    if player_y < 0:
        player_y = 0
    if player_y> screen_height - player_height:
        player_y = screen_height - player_height

    # --- Updated: Moving Enemy 1 ---
    enemy1_x += enemy1_speed
    if enemy1_x >= screen_width - enemy1_width or enemy1_x <= 0:
        enemy1_speed *= -1
    enemy1_y += enemy1_speed
    if enemy1_y >= screen_height - enemy1_height or enemy1_y <= 0:
        enemy1_speed *= -1

    # --- New: Moving Enemy 2 ---
    enemy2_x += enemy2_speed
    if enemy2_x >= screen_width - enemy2_width or enemy2_x <= 0:
        enemy2_speed *= -1
    enemy2_y += enemy2_speed
    if enemy2_y >= screen_height - enemy2_height or enemy2_y <= 0:
        enemy2_speed *= -1


    # --- Updated: Collision detection with Enemy 1 or Enemy 2 ---
    player_hit = False
    if is_collision(player_x, player_y, enemy1_x, enemy1_y, player_width, enemy1_width):
        player_hit = True
    elif is_collision(player_x, player_y, enemy2_x, enemy2_y, player_width, enemy2_width):
        player_hit = True

    if player_hit:
        lives -= 1
        if lives == 0:
            print(f"Game Over! Final Score: {score}")
            running = False
        else:
            # Reset player and both enemies after collision if lives remain
            player_x = 370
            enemy1_x = 200
            enemy1_speed *= -1  # Ensure enemy moves away from player after collision reset
            enemy2_x = 600  # Reset enemy 2 as well
            enemy2_speed *= -1  # Ensure enemy 2 moves away

    # Coin collision detection
    if coin_active and is_collision(player_x, player_y, coin_x, coin_y, player_width, coin_width):
        score += coin_value
        coin_active = False
        respawn_timer_start = pygame.time.get_ticks()
        print(f"Coin collected! Score: {score}")

    # Check for coin respawn
    if not coin_active:
        current_time = pygame.time.get_ticks()
        if current_time - respawn_timer_start >= respawn_delay:
            coin_x = random.randint(0, screen_width - coin_width)
            coin_y = random.randint(100, screen_height - 200)
            coin_active = True
            print("Coin respawned!")

    # Fill the screen with background color
    screen.fill((0, 0, 255))  # Blue background

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # Draw Enemy 1
    pygame.draw.rect(screen, enemy1_color, (enemy1_x, enemy1_y, enemy1_width, enemy1_height))

    # --- New: Draw Enemy 2 ---
    pygame.draw.rect(screen, enemy2_color, (enemy2_x, enemy2_y, enemy2_width, enemy2_height))

    # Draw the coin if active
    if coin_active:
        pygame.draw.rect(screen, coin_color, (coin_x, coin_y, coin_width, coin_height))

    # Display Score and Lives
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (screen_width - lives_text.get_width() - 10, 10))

    pygame.display.update()

pygame.quit()
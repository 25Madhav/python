import random
import pygame
pygame.init()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("COLLECT THE COINS TO WIN!")
player_x = 370
player_y = 480
player_speed = 0.3
player_width = 50
player_height = 50
player_color = (255, 0, 0)
enemy_width = 50
enemy_height = 50
enemies = []
enemy_colors = [(0, 255, 0), (255, 165, 0), (0, 255, 255), (255, 0, 255), (128, 0, 128), (0, 128, 128), (255, 255, 0)]
for i in range(7):
    enemy = {
        'x': random.randint(0, screen_width - enemy_width),
        'y': random.randint(50, screen_height // 2 - enemy_height),  
        'speed_x': random.choice([-1, 1]) * (random.random() * 0.4 + 0.2),  
        'speed_y': random.choice([-1, 1]) * (random.random() * 0.4 + 0.2),  
        'color': enemy_colors[i % len(enemy_colors)] 
    }
    enemies.append(enemy)
    score = 0
    lives = 3
    font = pygame.font.Font(None, 36)
    coin_width = 30
coin_height = 30
coin_color = (255, 223, 0)  # yellow
coin_value = 1000

coin_x = random.randint(0, screen_width - coin_width)
coin_y = random.randint(100, screen_height - 200)
coin_active = True
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
            running=False
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
if player_y > screen_height - player_height:
    player_y = screen_height - player_height

# --- Updated: Moving all enemies ---
for enemy in enemies:
    enemy['x'] += enemy['speed_x']
    enemy['y'] += enemy['speed_y']

    if enemy['x'] >= screen_width - enemy_width or enemy['x'] <= 0:
        enemy['speed_x'] *= -1
    if enemy['y'] >= screen_height - enemy_height or enemy['y'] <= 0:
        enemy['speed_y'] *= -1

# --- Updated: Collision detection with any enemy ---
player_hit = False
for enemy in enemies:
    if is_collision(player_x, player_y, enemy['x'], enemy['y'], player_width, enemy_width):
        player_hit = True
        break # No need to check other enemies if one collision is found

if player_hit:
    lives -= 1
    if lives == 0:
        print(f"Game Over! Final Score: {score}")
        running = False
    else:
        # Reset player and all enemies after collision if lives remain
        player_x = 370
        for enemy in enemies:
            enemy['x'] = random.randint(0, screen_width - enemy_width)
            enemy['y'] = random.randint(50, screen_height // 2 - enemy_height)
            enemy['speed_x'] *= -1 # Ensure enemy moves away from player after collision reset
            enemy['speed_y'] *= -1


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
screen.fill((0, 0, 255)) # Blue background

# Draw the player
pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

# --- Updated: Draw all enemies ---
for enemy in enemies:
    pygame.draw.rect(screen, enemy['color'], (enemy['x'], enemy['y'], enemy_width, enemy_height))

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
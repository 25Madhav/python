import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Correctly assign set_mode and set_caption separately
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Avoiding and Color-Changing Sprites")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

ALL_COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE, PURPLE]

SPRITE_SIZE = 50
SPRITE_SPEED = 3

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

class BouncingSprite:
    # Use the correct constructor name
    def __init__(self, x, y, size, speed_x, speed_y, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x *= -1
            # Removed HTML tags
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT, {'sprite': self}))
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y *= -1
            # Removed HTML tags
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT, {'sprite': self}))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def change_color(self):
        new_color = random.choice(ALL_COLORS)
        while new_color == self.color:
            new_color = random.choice(ALL_COLORS)
        self.color = new_color  # Assign after loop

sprite1 = BouncingSprite(100, 100, SPRITE_SIZE, SPRITE_SPEED, SPRITE_SPEED, RED)
sprite2 = BouncingSprite(SCREEN_WIDTH - 100 - SPRITE_SIZE, SCREEN_HEIGHT - 100 - SPRITE_SIZE, SPRITE_SIZE, -SPRITE_SPEED, -SPRITE_SPEED, BLUE)

clock = pygame.time.Clock()
FPS = 60
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR_EVENT:
            event.sprite.change_color()

    sprite1.move()
    sprite2.move()

    # Avoidance logic: bounce on collision
    if sprite1.rect.colliderect(sprite2.rect):
        sprite1.speed_x *= -1
        sprite1.speed_y *= -1
        sprite2.speed_x *= -1
        sprite2.speed_y *= -1

        # Removed HTML tags
        pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT, {'sprite': sprite1}))
        pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT, {'sprite': sprite2}))

    screen.fill(BLACK)
    sprite1.draw(screen)
    sprite2.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
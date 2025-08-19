import math
import random
import pygame
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_MIN_Y=50
ENEMY_START_MAX_Y=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED=10
COLLISION_DISTANCE=27
pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("space invaders")
icon=pygame.image.load("ufo")
pygame.display.set_icon(icon)
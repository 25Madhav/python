import pygame
pygame.init()
window=pygame.display.set_mode((400,400))
window.fill((255,255,255))
Green=(125,125,255)
pygame.draw .circle(window,Green,(300,300),50)
pygame.draw .circle(window,Green,(100,100),50,3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
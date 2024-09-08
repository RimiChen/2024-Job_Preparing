import pygame
### object shapes
from GameAI_Shapes_Character import *

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Testing Game AI")
### x,y, w,h
player = pygame.Rect((300, 250, 50, 50))

run = True

# while run:
while run == True:
    ### color, for refresh
    screen.fill((0,0,0))
    
    ### container, color, object
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] ==True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] ==True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] ==True:
        player.move_ip(0, 1)
    
    
    
    ### Control game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
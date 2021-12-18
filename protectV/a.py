import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.screen.set_caption("Title")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)

import pygame
import config
class HeroSprite(pygame.sprite.Sprite):
    def __init__(self, screen, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
    def update(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))



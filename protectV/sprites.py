import pygame
import config as cfg
import math


class HeroSprite(pygame.sprite.Sprite):
    def __init__(self, screen, image, position):
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.angle = 0

    def update(self):
        # 四个按键控制角色上下左右移动
        key_pressed = pygame.key.get_pressed()
        self.speed = 5
        if key_pressed[pygame.K_a]:
            self.rect.left = max(self.rect.left - self.speed, 0)
        elif key_pressed[pygame.K_d]:
            self.rect.left = min(self.rect.left + self.speed, cfg.SCREENSIZE[0] - 80)
        elif key_pressed[pygame.K_w]:
            self.rect.top = max(self.rect.top - self.speed, 0)
        elif key_pressed[pygame.K_s]:
            self.rect.top = min(self.rect.top + self.speed, cfg.SCREENSIZE[1] - 80)
        # 鼠标控制英雄转动
        mouse_pos = pygame.mouse.get_pos()
        angle = math.atan2(mouse_pos[1] - (self.rect.top + 32), mouse_pos[0] - (self.rect.left + 26))
        image_rotate = pygame.transform.rotate(self.image, 360 - angle * 57.29)
        bunny_pos = (
            self.rect.left - image_rotate.get_rect().width / 2, self.rect.top - image_rotate.get_rect().height / 2)
        self.rotated_position = bunny_pos
        self.screen.blit(image_rotate, bunny_pos)


class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, radius, position):
        super().__init__()
        self.radius = radius
        self.angle = 360 - self.radius * 57.29
        self.image = pygame.transform.rotate(image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 7

    def update(self):
        self.rect.left += self.speed * math.cos(math.radians(self.angle))
        self.rect.top += self.speed * math.sin(math.radians(self.angle))
        if self.rect.right < 0 or self.rect.left > cfg.SCREENSIZE[0] \
                or self.rect.top > cfg.SCREENSIZE[1] or self.rect.bottom < 0:
            self.kill()

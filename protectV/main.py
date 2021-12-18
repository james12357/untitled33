import pygame
import config
import sys
import sprites
def initGame():
    # 初始化pygame, 设置展示窗口
    pygame.init()
    screen = pygame.display.set_mode(config.SCREENSIZE)
    # 初始化mixer
    pygame.mixer.init()
    pygame.display.set_caption('保卫水晶')
    # 加载必要的游戏素材
    game_images = {}
    game_sound = {}
    for key, value in config.Image_Paths.items():
        game_images[key] = pygame.image.load(value)
    for key, value in config.Sound_Paths.items():
        game_sound[key] = pygame.mixer.Sound(value)
    return screen, game_images, game_sound
def main():
    # 初始化
    screen, game_images, game_sound = initGame()
    background = game_images['bg']
    background = pygame.transform.scale(background, (1000, 700))
    hero = sprites.HeroSprite(screen, image=game_images.get('role'), position=(150, 300))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 添加背景
        screen.blit(background, (0, 0))
        # 添加基地
        for i in range(1,5):
            screen.blit(game_images['base'], (0, 100 * i))
        #给游戏界面添上英雄
        hero.update()
        pygame.display.update()
main()





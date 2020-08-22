#Made by StreetArtist
import pygame
#导入pygame库
from sys import exit
#向sys模块借一个exit函数用来退出程序

pygame.mixer.init()
pygame.init()
pygame.font.init()
#初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((800, 600), 0, 32)
#创建了一个窗口,窗口大小和背景图片大小一样
pygame.display.set_caption("Fast calculation速算")
#设置窗口标题
background = pygame.image.load('bg.jpg').convert()
#加载并转换图像

pygame.mixer.music.load("suan.ogg")
pygame.mixer.music.play(-1)

sound = pygame.mixer.Sound("warring.wav")

myfont = pygame.font.SysFont('SimHei', 30)

info = myfont.render('速算训练', False, (0, 0, 0))

while True:
#游戏主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #接收到退出事件后退出程序
            pygame.quit()
            exit()
    screen.blit(background, (0,0))
    screen.blit(info, (0,0))
    #将背景图画上去
    pygame.display.update()
    #刷新一下画面

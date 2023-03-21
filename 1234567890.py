import dbm
import os
import sys
import time
import pygame
import random
from pygame import font
from pygame import QUIT

cur = os.path.dirname(os.path.abspath(__file__))
spr = os.path.join(cur, "sprite")
sys.path.append(cur)
sys.path.append(spr)
from baozha import *
from zidan import *
from wanjia import *
from diren import *

WI = 480
HI = 680
FPS = 30
I_sp = 12
bullet_sp = 50
hig = 'high_score'
sco = 'score'
db = 'db/game.db'

screen = pygame.display.set_mode((WI, HI))

pygame.mouse.set_visible(False)

pygame.display.set_caption('飞机大战-python-pygame')

micon = pygame.image.load('G:/编程/看漫画学Python/Icon-50.png')
pygame.display.set_icon(micon)


def main():
    direnshangxian = 5
    aaaaaa = 0
    pygame.init()
    done = False
    cos = pygame.time.Clock()
    ajj = 0
    ajjj = 0
    jifen = 0
    myim = pygame.image.load('G:/编程/看漫画学Python/hero.png')
    my = He(image=myim, x=150, y=600)

    He_zu = pygame.sprite.Group()
    He_zu.add(my)

    zidan_zu = pygame.sprite.Group()

    diren_zu = pygame.sprite.Group()
    
    while not done:
        
        print(len(diren_zu), ajj,my.rect.x,my.rect.y)
        ajj += 11
        ajjj += 1
        if ajjj == 200:
            ajjj = 0
            direnshangxian += 1
        if ajj >= 30:
            ajj = 0
            if len(diren_zu) <= direnshangxian:
                lei = random.randint(1, 4)
                diren = En(type=lei)
                diren_zu.add(diren)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                exit()
        
        v = pygame.key.get_pressed()
        if v[pygame.K_a]:
            my.rect.move_ip(-I_sp, 0)
            if my.rect.x <= 0:
                my.rect.x = 0

        if v[pygame.K_d]:
            my.rect.move_ip(I_sp, 0)
            if my.rect.x + my.rect.width >= WI:
                my.rect.x = WI - my.rect.width

        if v[pygame.K_w]:
            my.rect.move_ip(0, -I_sp)
            if my.rect.y <= 0:
                my.rect.y = 0

        if v[pygame.K_s]:
            my.rect.move_ip(0, I_sp)
            if my.rect.y + my.rect.height >= HI:
                my.rect.y = HI - my.rect.height

        if v[pygame.K_q]:
            zi = zidan(speed=30, x=my.rect.x, y=my.rect.y)
            zidan_zu.add(zi)
            zi = zidan(speed=30, x=my.rect.x + my.rect.width, y=my.rect.y)
            zidan_zu.add(zi)

        zi = zidan(speed=30, x=my.rect.x +(my.rect.width / 2), y=my.rect.y)
        zidan_zu.add(zi)

        ene = diren_zu.sprites()
        for enemy in ene:
            hi = pygame.sprite.spritecollide(enemy, zidan_zu, True)
            if hi:
                zidan.visible = False

                enemy.hit -= 1
                if enemy.hit <= 0 and aaaaaa == 0:
                    enemy.visible = False
                    jifen += ensc[enemy.type]
                    exp = Ex(enemy.rect.center)
                    He_zu.add(exp)

        for q in diren_zu:
            isa = pygame.sprite.collide_rect(q, my)
            if isa:
                He_zu.remove(my)
                my.visible = False
                aaaa = pygame.image.load('G:/编程/看漫画学Python/game over-680.png')
                screen.blit(aaaa, (0, 0))
                font2 = font.Font("G:/编程/看漫画学Python/ALGER.TTF", 40)
                text3 = font2.render(str(jifen), True, (255, 255, 255))
                screen.blit(text3, (200, 530))
                pygame.display.update()
                aaaaaa = 1
                pygame.mouse.set_visible(True)

        beijing = pygame.image.load('G:/编程/看漫画学Python/480x680.png')
        screen.blit(beijing, (0, 0))

        font1 = font.Font("G:/编程/看漫画学Python/ALGER.TTF", 20)

        text1 = font1.render(str('x:') + str(my.rect.x), True, (255, 255, 255))
        screen.blit(text1, (10, 10))
        text2 = font1.render(str('y:') + str(my.rect.y), True, (255, 255, 255))
        screen.blit(text2, (10, 40))
        font2 = font.Font("G:/编程/看漫画学Python/ALGER.TTF", 40)
        text3 = font2.render(str(str('score:') + str(jifen)), True, (255, 255, 255))
        screen.blit(text3, (170, 70))
        zidan_zu.draw(screen)
        zidan_zu.update()
        diren_zu.draw(screen)
        diren_zu.update()
        He_zu.draw(screen)
        He_zu.update()

        if aaaaaa == 0:
            pygame.display.update()
        cos.tick(FPS)


if __name__ == '__main__':
    main()

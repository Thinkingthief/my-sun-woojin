import pygame as pg
import sys
import random

pg.init()
screen = pg.display.set_mode((1000,400))

r1 = pg.Rect(50, 50, 50, 50)
r2 = pg.Rect(200, 50, 50, 50)

bg = pg.image.load('images/bg.png')
rr = pg.image.load('images/rr.png')
potion = pg.image.load('images/potion.png')
fire =pg.image.load('images/fire.png')
mob = pg.image.load('images/mob.png')
win = pg.image.load('images/win.png')

x = random.randint(500,650,)
y = random.randint(0, 50)
r4 = pg.Rect(x, y, 50, 50)

magic = False
fire_on = False

def move(r):
    if key[pg.K_RIGHT]:
        r.x = r.x + 1
    if key[pg.K_LEFT]:
        r.x = r.x - 1
    if key[pg.K_UP]:
        r.y = r.y - 1
    if key[pg.K_DOWN]:
        r.y = r.y + 1

pg.mixer.Sound('sounds/powerup.wav').play()
        
while True :
    screen.blit(bg, (0,0))
    key = pg.key.get_pressed()
    move(r1)
    screen.blit(rr, r1)

    if magic ==True and r3.colliderect(r4):
        screen.blit(win, r4)
        pg.mixer.Sound('sounds/stage_clear.wav').play()
        pg.display.update()
        pg.time.delay(5500)
        pg.quit()
        sys.exit

    
    screen.blit(mob, r4)
    r4.x = r4.x - 0.5

    if magic == False:
        screen.blit(potion, r2)
        if r1.colliderect(r2):
            magic = True
            r3 = pg.Rect(r1.x + 65, r1.y +25, 50, 50)
            pg.mixer.Sound('sounds/powerup2.wav').play()
    else:
        if key[pg.K_SPACE]:
            fire_on =True
            pg.mixer.Sound('sounds/powerup2.wav').play()
        screen.blit(fire, r3)
        if fire_on:
            r3.x = r3.x + 1
        else:
            move(r3)
        
    pg.display.update()
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit()

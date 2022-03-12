import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((1000,400))

bg = pg.image.load('images/bg.png')
rr = pg.image.load('images/rr.png')

x = 20
y = 20
magic = False

while True :
    screen.blit(bg,(0,0))
    screen.blit(rr,(x,y))
    key = pg.key.get_pressed()
    
    if key[pg.K_RIGHT] :
        x = x + 1

    if key[pg.K_LEFT] :
        x = x - 1
        
    if key[pg.K_UP] :
        y = y - 1

    if key[pg.K_DOWN] :
        y = y + 1


    if key[pg.K_RETURN] :
        if magic == False :
            rr.set_alpha(100)
            magic = True
        else :
            rr.set_alpha(255)
            magic = False
     
    pg.display.update()

    for event in pg.event.get() :
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit()

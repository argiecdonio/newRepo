import pygame as pg

pg.init()
screen_width = 900
screen_height = 507

x_pos = 0
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("moving background with sprite")

background = pg.image.load("imgs/bg.jpg")
walkleft = [
    pg.image.load("imgs/l1.png"), pg.image.load("imgs/l2.png"),
    pg.image.load("imgs/l3.png"), pg.image.load("imgs/l4.png"),
    pg.image.load("imgs/l5.png"), pg.image.load("imgs/l6.png"),
]
walkright = [
    pg.image.load("imgs/r1.png"), pg.image.load("imgs/r2.png"),
    pg.image.load("imgs/r3.png"), pg.image.load("imgs/r4.png"),
    pg.image.load("imgs/r5.png"), pg.image.load("imgs/r6.png"),
]
idleleft = pg.image.load("imgs/standleft.png")
idleright = pg.image.load("imgs/standright.png")
lastposition = "right"
left = False
right = False
framecount = 0
def drawsprite(vertical_loc):
    global framecount
    if framecount + 1 > 6:
        framecount = 0
    if left:
        screen.blit(walkleft[framecount],(screen_width/2,vertical_loc))
    elif right:
        screen.blit(walkright[framecount], (screen_width / 2, vertical_loc))
    else:
        if lastposition == "left":
            screen.blit(idleleft, (screen_width / 2, vertical_loc))
        elif lastposition == "right":
            screen.blit(idleright, (screen_width / 2, vertical_loc))
    framecount += 1

run = True
while run:
    screen.blit(background,(0,0))
    rel_x = x_pos % background.get_rect().width
    screen.blit(background,(rel_x - background.get_rect().width,0))
    if rel_x < screen_width:
        screen.blit(background,(rel_x, 0))

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x_pos += 1
        left = True
        right = False
        lastposition = "left"
    elif keys[pg.K_RIGHT]:
        x_pos -= 1
        left = False
        right = True
        lastposition = "right"
    else:
        left = False
        right = False

    drawsprite(380)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()
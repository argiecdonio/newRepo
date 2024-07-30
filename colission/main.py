
import pygame as pg
import random

pg.init()
screen_width = 1000
screen_height = 700
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("sample game collision")

mainchar = pg.Rect(0,0,25,25)
obstacle = []
for _ in range(20):
    obstacle_rect = pg.Rect(random.randint(1,999),
                      random.randint(1,699), 25,25)
    obstacle.append(obstacle_rect)

bg = (25,25,25)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

pg.mouse.set_visible(False)
run = True
while run:
    screen.fill(bg) # to set backgound first

    col = green
    for obs in obstacle:
        if mainchar.colliderect(obs):
            col = red

    position = pg.mouse.get_pos()
    mainchar.center = position

    pg.draw.rect(screen, col, mainchar)
    for obs in obstacle:
        pg.draw.rect(screen, blue, obs)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()

import pygame
import csv
from image_sprite import SpriteSheet #import python file image_sprite.py with SpritSheet class

WIDTH = 960
HEIGHT = 640
blocksize = 32

screen = pygame.display.set_mode((WIDTH, HEIGHT))
sprites = SpriteSheet("tileset_image.png") # calling the class with argument/parameter of image file
img = pygame.image.load("tileset_image.png").convert() # convert the image to get properties

background = pygame.image.load("bakground.jpg")
bakresize = pygame.transform.scale(background, (WIDTH,HEIGHT))

#blocklist = []
tilelist = []
imagetiles = []
csvdata = []
for y in range(0, img.get_height(), blocksize): # this loop is getting the row position by pixel
    for x in range(0, img.get_width(), blocksize): # this loop is getting the column position by pixel
        #print("x:", x, "y:",y)
        imagetiles.append(sprites.get_image(x, y, blocksize, blocksize)) # appending a list array of tile images from Sprite object (get_image function is from SpriteSheet class)

"""
for x in range(0, WIDTH, blocksize):
    for y in range(0, HEIGHT, blocksize):
        blocklist.append([x,y])
"""

def drawgrid(): # the result of this function is to display grid to the screen
    for x in range(0, WIDTH, blocksize): #this loop getting the column position by pixel
        for y in range(0, HEIGHT, blocksize): #this loop getting the row position by pixel
            rect = pygame.Rect(x,y,blocksize,blocksize) # creating rect
            pygame.draw.rect(screen,(50,50,50), rect, 1) # draw the rect to the screen


def readcsv():
    map = []
    with open("map1.csv") as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map.append(list(row))
    return map

run = True
while run:
    #screen.fill((0,0,0))
    screen.blit(bakresize, (0,0))
    #drawgrid()

    x, y, counter = 0, 0, 0
    for row in readcsv():
        x = 0
        for tile in row:
            if tile == '-1':
                c = 1+1
            else:
                #screen.blit(imagetiles[counter], (blocklist[counter][0], blocklist[counter][1]))
                #screen.blit(imagetiles[int(tile)],(x * blocksize, y * blocksize))
                screen.blit(imagetiles[int(tile)], (x * blocksize, y * blocksize))
            x += 1
        # Move to next row
        y += 1

    #screen.blit(sprites.get_image(32,32,blocksize,blocksize),(0,0))


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
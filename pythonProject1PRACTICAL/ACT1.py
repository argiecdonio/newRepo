import pygame
pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("gihu na square ayy")


rect_x = 250
rect_y = 150

rect_width = 50
rect_height = 50

movement_speed = 5

rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)


running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rect.y -= movement_speed
            elif event.key == pygame.K_DOWN:
                rect.y += movement_speed
            elif event.key == pygame.K_LEFT:
                rect.x -= movement_speed
            elif event.key == pygame.K_RIGHT:
                rect.x += movement_speed


    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), rect)

    pygame.display.update()


pygame.quit()


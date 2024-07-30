import pygame

SCREEN_HEIGHT = 400
SCREEN_WIDTH =500

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption('Button')


start_img = pygame.image.load('venv/start_btn.png').convert_alpha()
exit_img = pygame.image.load('venv/exit_btn.png').convert_alpha()

class Button:
    def __init__(self,x ,y ,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        screen.blit(self.image, (self.rect.x, self.rect.y))

start_button = Button(100, 200, start_img)
exit_button = Button (450, 200, exit_img)

run = True
while run:

    screen.fill((202, 228, 241))

    start_button.draw()
    exit_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
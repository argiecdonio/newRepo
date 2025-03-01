import pygame
import random

pygame.init()
screen = pygame.display.set_mode((900, 600))
# background
background = pygame.image.load('13.jpg')
white = (250, 250, 250)
red = (200, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 1000
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen.blit(background, (0, 0))
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 1
    velocity_y = 1
    snk_list = []
    snk_length = 2

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(60, screen_height - 20)
    score = 0
    init_velocity = 4
    snake_size = 30
    fps = 90  # fps = frames per second
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game over! Press Enter To Play Again", red, 200, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0


                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0


                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 1
                food_x = random.randint(20, screen_width - 30)
                food_y = random.randint(60, screen_height - 30)
                snk_length += 5

            gameWindow.fill(white)
            text_screen("Score: " + str(score * 10), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gameWindow, red, (0, 40), (900, 40), 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width - 20 or snake_y < 50 or snake_y > screen_height - 20:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


gameloop()

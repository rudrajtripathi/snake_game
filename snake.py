import pygame
from pygame.locals import *
import random

pygame.init()

red = (255, 0, 0)
dark_red = (139, 0, 0)
golden_yellow = (255, 185, 15)
dark_green = (0, 100, 0)

win_width = 600
win_height = 400

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

snake = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

def user_score(score):
    nmbr = score_font.render("Score :" + str(score), True, red)
    window.blit(nmbr, [0, 0])

def game_snake(snake, snake_len_list):
    for x in snake_len_list:
        pygame.draw.rect(window, golden_yellow, [x[0], x[1], snake, snake])

def message(msg):
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width / 20, win_height / 3])

def game_loop():
    gameOver = False
    gameClose = False
    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_len_list = []
    snake_len = 1

    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    while not gameOver:

        while gameClose == True:
            window.fill(dark_green)
            message("You lost!! press 'P' to play and 'Q' to quit the game")
            user_score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                if event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake
                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake

        if x1 > win_width or x1 < 0 or y1 > win_height or y1 < 0:
            gameClose = True

        x1 += x1_change
        y1 += y1_change
        window.fill(dark_green)
        pygame.draw.rect(window, dark_red, [foodx, foody, snake, snake])

        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_len_list.append(snake_size)

        if len(snake_len_list) > snake_len:
            del snake_len_list[0]

        game_snake(snake, snake_len_list)
        user_score(snake_len - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_len += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
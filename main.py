import pygame
import sys
from snakegame import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    #Objects
    snake = Snake()
    object = Object()
    background = Background()
    colission = Colission()
    points = Points()
    
    #Main loop
    while True:
        background.draw(screen)
        snake.draw(screen)
        object.draw(screen)
        points.show(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if snake.state != "Down":
                        snake.state = "Up"

                if event.key == pygame.K_s:
                    if snake.state != "Up":
                        snake.state = "Down"

                if event.key == pygame.K_a:
                    if snake.state != "Right":
                        snake.state = "Left"

                if event.key == pygame.K_d:
                    if snake.state != "Left":
                        snake.state = "Right"

                if event.key == pygame.K_ESCAPE:
                    snake.state = "Stop"

        if colission.between_snake_and_apple(snake, object):
            object.spawn()
            snake.add_body()
            points.increase()

        #Movement
        if snake.state != "Stop":
            snake.move_body()        
            snake.move_head()

        if colission.between_snake_and_walls(snake):
            #lose
            snake.die()
            object.spawn()
            points.reset()

        if colission.between_head_and_body(snake):
            #lose
            snake.die()
            object.spawn()
            points.reset()

        pygame.time.delay(110)
        pygame.display.update()

main()
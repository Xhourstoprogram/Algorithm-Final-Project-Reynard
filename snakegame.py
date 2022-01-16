import pygame
import math
import random
from settings import *

#Creating the snake
class Snake:

    def __init__(self):
        self.color = blue
        self.headX = random.randrange(0, width, pixels)
        self.headY = random.randrange(0, height, pixels)
        self.bodies = []
        self.body_color = 50
        self.state = "Stop" #Stop, Up, Down, Left, Right

    def move_head(self):
        if self.state == "Up":
            self.headY -= pixels

        elif self.state == "Down":
            self.headY += pixels

        elif self.state == "Left":
            self.headX -= pixels

        elif self.state == "Right":
            self.headX += pixels

    def move_body(self):
        if len(self.bodies) > 0:
            for i in range(len(self.bodies)-1, -1, -1):
                if i == 0:
                    self.bodies[0].posX = self.headX
                    self.bodies[0].posY = self.headY
                else:
                    self.bodies[i].posX = self.bodies[i - 1].posX
                    self.bodies[i].posY = self.bodies[i - 1].posY
    
    def add_body(self):
        self.body_color += 10
        body = Body((0, 0, self.body_color), self.headX, self.headY)
        self.bodies.append(body)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.headX, self.headY, pixels, pixels))
        if len(self.bodies) > 0:
            for body in self.bodies:
                body.draw(surface)

    def die(self):
        self.headX = random.randrange(0, width, pixels)
        self.headY = random.randrange(0, height, pixels)
        self.bodies = []
        self.body_color = 50
        self.state = "Stop"

#Making the snake's body
class Body:

    def __init__(self, color, posX, posY):
        self.color = color
        self.posX = posX
        self.posY = posY

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX, self.posY, pixels, pixels))

#Creating the object
class Object:

    def __init__(self):
        self.color = red
        self.spawn()

    def spawn(self):
        self.posX = random.randrange(0, width, pixels)
        self.posY = random.randrange(0, height, pixels)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX, self.posY, pixels, pixels))

#Making the background
class Background:

    def draw(self, surface):
        surface.fill(BG1)
        counter = 0
        for row in range(squares):
            for col in range(squares):
                if counter % 2 == 0:
                    pygame.draw.rect(surface, BG2, (col * pixels, row * pixels, pixels, pixels))
                if col != squares - 1:
                    counter += 1
        
class Colission:

    def between_snake_and_apple(self, snake, apple):
        distance = math.sqrt(math.pow((snake.headX - apple.posX), 2) + math.pow((snake.headY - apple.posY), 2))
        return distance < pixels

    def between_snake_and_walls(self, snake):
        if snake.headX < 0 or snake.headX > width - pixels or snake.headY < 0 or snake.headY > height - pixels:
            return True
        return False

    def between_head_and_body(self, snake):
        for body in snake.bodies:
            distance = math.sqrt(math.pow((snake.headX - body.posX), 2) + math.pow((snake.headY - body.posY), 2))
            if distance < pixels:
                return True
        return False

#Giving the Points for each object that player gets with the snake
class Points:

    def __init__(self):
        self.points = 0
        self.font = pygame.font.SysFont("monospace", 30, bold=False)

    def increase(self):
        self.points += 10

    def reset(self):
        self.points = 0

    def show(self, surface):
        lbl = self.font.render("Points: " + str(self.points), 10, black)
        surface.blit(lbl, (5, 5))
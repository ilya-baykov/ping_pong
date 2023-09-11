import random

from COLORS import *
import time

import pygame


class GameField:
    WIDTH = 800
    HEIGHT = 800
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping-Pong")
    clock = pygame.time.Clock()
    clock.tick(60)

    @classmethod
    def draw(cls):
        cls.screen.fill((0, 0, 0))
        pygame.draw.line(cls.screen, GRAY, (0, cls.HEIGHT // 2), (cls.WIDTH, cls.HEIGHT // 2), 5)


class Platforms:
    size = 100

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.line(GameField.screen, self.color, (self.x - Platforms.size // 2, self.y),
                         (self.x + Platforms.size // 2, self.y), 4)

    def check_collision(self):
        if (self.x - Platforms.size // 2 < Ball.coordinates[0] < self.x + Platforms.size // 2 and Ball.coordinates[1] +
                Ball.size == self.y):
            print("КОНТАКТ!")
            return True


player_1 = Platforms(GameField.WIDTH // 2, 150, GREEN)
player_2 = Platforms(GameField.WIDTH // 2, GameField.HEIGHT - 150, BLUE)


class AngleDetection:
    pass


class Ball:
    coordinates = (GameField.WIDTH // 2, GameField.HEIGHT // 2)
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    color = RED
    size = 10

    @classmethod
    def draw(cls):
        pygame.draw.circle(GameField.screen, cls.color, cls.coordinates, 10)

    @classmethod
    def move(cls):
        cls.coordinates = cls.coordinates[0] + cls.dy, cls.coordinates[1] + cls.dx

    @classmethod
    def check_collision(cls):
        if cls.coordinates[0] >= GameField.WIDTH or cls.coordinates[0] <= 0:
            cls.dy = -cls.dy
        elif cls.coordinates[1] >= GameField.HEIGHT or cls.coordinates[1] <= 0:
            cls.dx = -cls.dx


class Collision:
    def check_platform(self):
        pass


class GameLoop:
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        GameField.draw()

        Ball.draw()
        Ball.move()
        Ball.check_collision()
        player_1.draw()
        player_2.draw()
        Platforms.check_collision(player_1)
        Platforms.check_collision(player_2)
        time.sleep(0.03)
        pygame.display.update()


GameLoop()

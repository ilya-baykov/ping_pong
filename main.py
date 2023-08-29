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


player_1 = Platforms(GameField.WIDTH // 2, 150, GREEN)
player_2 = Platforms(GameField.WIDTH // 2, GameField.HEIGHT - 150, BLUE)


class AngleDetection:
    pass


class Ball:
    coordinates = (GameField.WIDTH // 2, GameField.HEIGHT // 2)
    color = RED
    size = 10

    @classmethod
    def draw(cls):
        pygame.draw.circle(GameField.screen, cls.color, cls.coordinates, 10)

    @classmethod
    def drop(cls, side):
        cls.coordinates = cls.coordinates[0], cls.coordinates[1] + (cls.size * side)


class GameLoop:
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        GameField.draw()
        Ball.draw()
        Ball.drop(1)
        player_1.draw()
        player_2.draw()
        time.sleep(0.03)
        pygame.display.update()


GameLoop()

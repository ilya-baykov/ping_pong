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
        if (self.x - Platforms.size // 2 < Ball.coordinates[0] < self.x + Platforms.size // 2) and (
                (Ball.coordinates[1] + Ball.size == self.y) or (Ball.coordinates[1] - Ball.size == self.y)):
            print("КОНТАКТ!")
            Ball.dy = - Ball.dy
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
        cls.coordinates = cls.coordinates[0] + cls.dx, cls.coordinates[1] + cls.dy

    @classmethod
    def check_collision(cls):
        if cls.coordinates[0] >= GameField.WIDTH or cls.coordinates[0] <= 0:
            cls.dx = -cls.dx
        elif cls.coordinates[1] >= GameField.HEIGHT or cls.coordinates[1] <= 0:
            cls.dy = -cls.dy


class Collision:
    def check_platform(self):
        pass


class GameLoop:
    running = True
    move_left_1 = None
    move_left_2 = None
    button_1_press = False
    button_2_press = False
    button_key_1 = None
    button_key_2 = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    button_key_1 = "right"
                    button_1_press = True
                elif event.key == pygame.K_a:
                    button_key_1 = "left"
                    button_1_press = True
                elif event.key == pygame.K_RIGHT:
                    button_key_2 = "right"
                    button_2_press = True
                elif event.key == pygame.K_LEFT:
                    button_key_2 = "left"
                    button_2_press = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    button_1_press = False
                    button_key_1 = None
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    button_2_press = False
                    button_key_2 = None
        if button_1_press:
            if button_key_1 == "right":
                player_1.x += 10
            elif button_key_1 == "left":
                player_1.x -= 10
        if button_2_press:
            if button_key_2 == "right":
                player_2.x += 10
            elif button_key_2 == "left":
                player_2.x -= 10

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

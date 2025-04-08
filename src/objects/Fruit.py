import pygame
from pygame.math import Vector2
from random import randint



class Fruit:
    def __init__(self, cell_size, cell_number, screen):
        self.position_x = randint(0, cell_number - 1)
        self.position_y = randint(0, cell_number - 1)
        self.pos = Vector2(self.position_x, self.position_y)
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen


    def draw_fruit(self):
        fruit_rectangle = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, (90,255,100), fruit_rectangle)
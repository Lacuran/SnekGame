import pygame
from pygame.math import Vector2


class Snek:
    def __init__(self, cell_size, cell_number, screen):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen

    def draw_snek(self):
        for block in self.body:
            x_position = block.x * self.cell_size
            y_position = block.y * self.cell_size
            snek_rect = pygame.Rect(x_position, y_position, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen,(255,50,255), snek_rect)
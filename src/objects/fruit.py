import pygame
from pygame.math import Vector2
from random import randint

from src.main.base.base_setting_class import BaseSettingsClass


class Fruit(BaseSettingsClass):
    def __init__(self):
        super().__init__()
        self.position_x = randint(0, self.cell_number - 1)
        self.position_y = randint(0, self.cell_number - 1)
        self.pos = Vector2(self.position_x, self.position_y)


    def draw_fruit(self):
        fruit_rectangle = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size, self.cell_size)
        self.screen.blit(self.apple, fruit_rectangle)

    def randomize_position(self):
        self.__init__()
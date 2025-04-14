import pygame
from pygame.math import Vector2

from src.main.base.base_setting_class import BaseSettingsClass


class Snek(BaseSettingsClass):
    def __init__(self):
        super().__init__()
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1,0)
        self.new_body_block = False

    def draw_snek(self):
        for index, block in enumerate(self.body):
            x_position = block.x * self.cell_size
            y_position = block.y * self.cell_size
            block_rect = pygame.Rect(x_position, y_position, self.cell_size, self.cell_size)

            if index == 0:
                self.screen.blit(self.snek_head_left, block_rect)
            else:
                pygame.draw




    def move_snek(self):
        if self.new_body_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_body_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_body_block(self):
        self.new_body_block = True
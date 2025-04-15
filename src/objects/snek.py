import pygame
from pygame.math import Vector2

from src.main.base.base_setting_class import BaseSettingsClass


class Snek(BaseSettingsClass):
    def __init__(self):
        super().__init__()
        self.tail = None
        self.head = None
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1,0)
        self.new_body_block = False

    def draw_snek(self):
        self.update_head_graphic()
        self.update_tail_graphic()

        for index, block in enumerate(self.body):
            x_position = block.x * self.cell_size
            y_position = block.y * self.cell_size
            block_rect = pygame.Rect(x_position, y_position, self.cell_size, self.cell_size)

            if index == 0:
                self.screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                self.screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    self.screen.blit(self.snek_body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.screen.blit(self.snek_body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        self.screen.blit(self.snek_body_till_left, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        self.screen.blit(self.snek_body_bend_left, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        self.screen.blit(self.snek_body_till_right, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        self.screen.blit(self.snek_body_bend_right, block_rect)


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

    def update_head_graphic(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.snek_head_left
        if head_relation == Vector2(-1,0): self.head = self.snek_head_right
        if head_relation == Vector2(0,1): self.head = self.snek_head_up
        if head_relation == Vector2(0,-1): self.head = self.snek_head_down

    def update_tail_graphic(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.snek_tail_left
        if tail_relation == Vector2(-1, 0): self.tail = self.snek_tail_right
        if tail_relation == Vector2(0, 1): self.tail = self.snek_tail_up
        if tail_relation == Vector2(0, -1): self.tail = self.snek_tail_down

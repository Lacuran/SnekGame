import sys

import pygame

from src.objects.fruit import Fruit
from src.objects.snek import Snek

class Main:

    def __init__(self, cell_size, cell_number, screen):
        self.snek = Snek(cell_size, cell_number, screen)
        self.fruit = Fruit(cell_size, cell_number, screen)
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen

    def update(self):
        self.snek.move_snek()
        self.check_collision()
        self.check_for_failure()

    def draw_elements(self):
        self.snek.draw_snek()
        self.fruit.draw_fruit()

    def check_collision(self):
        if self.fruit.pos == self.snek.body[0]:
            self.fruit.randomize_position()
            self.snek.add_body_block()

    def check_for_failure(self):
        if not 0 <= self.snek.body[0].x < self.cell_number or not 0 <= self.snek.body[0].y < self.cell_number:
            self.game_over()

        for block in self.snek.body[1:]:
            if block == self.snek.body[0]:
                self.game_over()

    @staticmethod
    def game_over():
        pygame.quit()
        sys.exit()



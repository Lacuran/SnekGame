import pygame
import sys



class BaseWindowConfig:

    @staticmethod
    def get_pygame():
        return pygame

    @staticmethod
    def get_sys():
        return sys


    CELL_SIZE = 40
    CELL_NUMBER = 20
    SCREEN = get_pygame().display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
    CLOCK = get_pygame().time.Clock()


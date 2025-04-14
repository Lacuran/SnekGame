import pygame

class BaseWindowConfig:
    CELL_SIZE = 40
    CELL_NUMBER = 20
    SCREEN = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
    CLOCK = pygame.time.Clock()
import pygame

from src.main.base.base_window_config import BaseWindowConfig


class BaseAssetsConfig(BaseWindowConfig):
    APPLE = pygame.image.load('../../assets/body/apple.png').convert_alpha()
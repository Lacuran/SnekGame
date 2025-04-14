import pygame

from src.main.base.base_window_config import BaseWindowConfig


class BaseAssetsConfig(BaseWindowConfig):
    APPLE = pygame.image.load('../../assets/body/apple.png').convert_alpha()

    SNEK_TAIL_UP = pygame.image.load('../../assets/body/tail_up.png').convert_alpha()
    SNEK_TAIL_DOWN = pygame.image.load('../../assets/body/tail_down.png').convert_alpha()
    SNEK_TAIL_LEFT = pygame.image.load('../../assets/body/tail_left.png').convert_alpha()
    SNEK_TAIL_RIGHT = pygame.image.load('../../assets/body/tail_right.png').convert_alpha()

    SNEK_HEAD_UP = pygame.image.load('../../assets/body/head_up.png').convert_alpha()
    SNEK_HEAD_DOWN = pygame.image.load('../../assets/body/head_down.png').convert_alpha()
    SNEK_HEAD_LEFT = pygame.image.load('../../assets/body/head_left.png').convert_alpha()
    SNEK_HEAD_RIGHT = pygame.image.load('../../assets/body/head_right.png').convert_alpha()

    SNEK_BODY_BEND_LEFT = pygame.image.load('../../assets/body/body_bl.png').convert_alpha()
    SNEK_BODY_BEND_RIGHT = pygame.image.load('../../assets/body/body_br.png').convert_alpha()
    SNEK_BODY_TILL_LEFT = pygame.image.load('../../assets/body/body_tl.png').convert_alpha()
    SNEK_BODY_TILL_RIGHT = pygame.image.load('../../assets/body/body_tr.png').convert_alpha()

    SNEK_BODY_HORIZONTAL = pygame.image.load('../../assets/body/body_horizontal.png').convert_alpha()
    SNEK_BODY_VERTICAL = pygame.image.load('../../assets/body/body_vertical.png').convert_alpha()

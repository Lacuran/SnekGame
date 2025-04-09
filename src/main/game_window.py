import sys

import pygame
from pygame import Vector2

from src.main.main import Main

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
main_game = Main(cell_size, cell_number, screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game.game_over()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snek.direction.y != 1:
                    main_game.snek.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snek.direction.y != -1:
                    main_game.snek.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snek.direction.x != -1:
                    main_game.snek.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snek.direction.x != 1:
                    main_game.snek.direction = Vector2(-1, 0)
            if event.key == pygame.K_ESCAPE:
                main_game.game_over()


    screen.fill((210,180,50))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
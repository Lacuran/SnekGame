import pygame
from pygame import Vector2

from src.main.game.main import Main

pygame.init()
main_game = Main()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game.quit_game()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if main_game.snek.direction.y != 1:
                    main_game.snek.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snek.direction.y != -1:
                    main_game.snek.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snek.direction.x != -1:
                    main_game.snek.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if main_game.snek.direction.x != 1:
                    main_game.snek.direction = Vector2(-1, 0)
            if event.key == pygame.K_ESCAPE:
                main_game.quit_game()


    main_game.screen.fill((210,180,50))
    main_game.draw_elements()
    pygame.display.update()
    main_game.clock.tick(60)
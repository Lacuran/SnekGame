import pygame, sys

from src.objects.Fruit import Fruit
from src.objects.Snek import Snek

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fruit = Fruit(cell_size, cell_number, screen)
snek = Snek(cell_size, cell_number, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((210,180,50))
    fruit.draw_fruit()
    snek.draw_snek()
    pygame.display.update()
    clock.tick(60)
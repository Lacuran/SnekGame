from pygame import Vector2

from src.main.base.base_setting_class import BaseSettingsClass
from src.objects.fruit import Fruit
from src.objects.snek import Snek


class Main(BaseSettingsClass):
    def __init__(self):
        super().__init__()
        self.snek = Snek()
        self.fruit = Fruit()
        self.font = BaseSettingsClass.get_base_font()
        self.crunch_sound = BaseSettingsClass.get_base_crunch_sound()


    def update(self):
        self.snek.move_snek()
        self.check_collision()
        self.check_for_failure()

    def draw_elements(self):
        self.draw_grass()
        self.snek.draw_snek()
        self.fruit.draw_fruit()
        self.draw_score()


    def check_collision(self):
        if self.fruit.pos == self.snek.body[0]:
            self.fruit.randomize_position()
            self.snek.add_body_block()
            self.play_crunch_sound()

        for block in self.snek.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize_position()

    def check_for_failure(self):
        if not 0 <= self.snek.body[0].x < self.cell_number or not 0 <= self.snek.body[0].y < self.cell_number:
            self.game_over()

        for block in self.snek.body[1:]:
            if block == self.snek.body[0]:
                self.game_over()

    def draw_grass(self):
        grass_color = (167, 209, 67)
        for row in range(self.cell_number):
            if row % 2 == 0:
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        grass_rect = self.get_base_pygame().Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        self.get_base_pygame().draw.rect(self.screen, grass_color, grass_rect)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        grass_rect = self.get_base_pygame().Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        self.get_base_pygame().draw.rect(self.screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snek.body) - 3)
        score_surface = self.font.render(score_text, True, (56, 74, 12))
        score_x = self.cell_size * self.cell_number - 60
        score_y = self.cell_size * self.cell_number - 40
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        self.screen.blit(score_surface, score_rect)

    def play_crunch_sound(self):
        self.crunch_sound.play()


    def quit_game(self):
        print("Quit")
        self.get_base_pygame().quit()
        self.get_base_sys().exit()

    def game_over(self):
        self.snek.reset()




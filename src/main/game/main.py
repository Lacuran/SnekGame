from src.main.base.base_setting_class import BaseSettingsClass
from src.objects.fruit import Fruit
from src.objects.snek import Snek


class Main(BaseSettingsClass):
    def __init__(self):
        super().__init__()
        self.snek = Snek()
        self.fruit = Fruit()


    def update(self):
        self.snek.move_snek()
        self.check_collision()
        self.check_for_failure()

    def draw_elements(self):
        self.draw_grass()
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

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for column in range(self.cell_number):
            grass_rect = self.get_base_pygame().Rect(column * self.cell_size, 0 ,self.cell_size, self.cell_size)
            self.get_base_pygame().draw.rect(self.screen, grass_color, grass_rect)


    def game_over(self):
        print("Game Over")
        self.get_base_pygame().quit()
        self.get_base_sys().exit()




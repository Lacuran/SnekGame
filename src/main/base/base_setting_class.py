from src.main.base.base_assets_config import BaseAssetsConfig
from src.main.base.base_window_config import BaseWindowConfig


class BaseSettingsClass:
    def __init__(self):
        self.screen = BaseWindowConfig.SCREEN
        self.cell_size = BaseWindowConfig.CELL_SIZE
        self.cell_number = BaseWindowConfig.CELL_NUMBER
        self.clock = BaseWindowConfig.CLOCK

        self.apple = BaseAssetsConfig.APPLE

        self.snek_head_up = BaseAssetsConfig.SNEK_HEAD_UP
        self.snek_head_down = BaseAssetsConfig.SNEK_HEAD_DOWN
        self.snek_head_left = BaseAssetsConfig.SNEK_HEAD_LEFT
        self.snek_head_right = BaseAssetsConfig.SNEK_HEAD_RIGHT

        self.snek_body_bend_left = BaseAssetsConfig.SNEK_BODY_BEND_LEFT
        self.snek_body_bend_right = BaseAssetsConfig.SNEK_BODY_BEND_RIGHT
        self.snek_body_till_left = BaseAssetsConfig.SNEK_BODY_TILL_LEFT
        self.snek_body_till_right = BaseAssetsConfig.SNEK_BODY_TILL_RIGHT

        self.snek_body_horizontal = BaseAssetsConfig.SNEK_BODY_HORIZONTAL
        self.snek_body_vertical = BaseAssetsConfig.SNEK_BODY_VERTICAL

        self.snek_tail_up = BaseAssetsConfig.SNEK_TAIL_UP
        self.snek_tail_down = BaseAssetsConfig.SNEK_TAIL_DOWN
        self.snek_tail_left = BaseAssetsConfig.SNEK_TAIL_LEFT
        self.snek_tail_right = BaseAssetsConfig.SNEK_TAIL_RIGHT

    @staticmethod
    def get_base_pygame():
        return BaseWindowConfig.get_pygame()

    @staticmethod
    def get_base_sys():
        return BaseWindowConfig.get_sys()

    @staticmethod
    def get_base_vector2():
        return BaseWindowConfig.get_vector2()
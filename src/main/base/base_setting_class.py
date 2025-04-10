from src.main.base.base_config import BaseConfig


class BaseSettingsClass:
    def __init__(self):
        self.screen = BaseConfig.SCREEN
        self.cell_size = BaseConfig.CELL_SIZE
        self.cell_number = BaseConfig.CELL_NUMBER
        self.clock = BaseConfig.CLOCK
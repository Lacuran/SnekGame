from src.main.base.base_assets_config import BaseAssetsConfig
from src.main.base.base_window_config import BaseWindowConfig


class BaseSettingsClass:
    def __init__(self):
        self.screen = BaseWindowConfig.SCREEN
        self.cell_size = BaseWindowConfig.CELL_SIZE
        self.cell_number = BaseWindowConfig.CELL_NUMBER
        self.clock = BaseWindowConfig.CLOCK
        self.apple = BaseAssetsConfig.APPLE
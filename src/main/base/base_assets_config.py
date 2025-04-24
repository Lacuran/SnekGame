from src.main.base.base_window_config import BaseWindowConfig


class BaseAssetsConfig(BaseWindowConfig):
    APPLE = BaseWindowConfig.get_pygame().image.load('../../assets/body/apple.png').convert_alpha()

    SNEK_TAIL_UP = BaseWindowConfig.get_pygame().image.load('../../assets/body/tail_up.png').convert_alpha()
    SNEK_TAIL_DOWN = BaseWindowConfig.get_pygame().image.load('../../assets/body/tail_down.png').convert_alpha()
    SNEK_TAIL_LEFT = BaseWindowConfig.get_pygame().image.load('../../assets/body/tail_left.png').convert_alpha()
    SNEK_TAIL_RIGHT = BaseWindowConfig.get_pygame().image.load('../../assets/body/tail_right.png').convert_alpha()

    SNEK_HEAD_UP = BaseWindowConfig.get_pygame().image.load('../../assets/body/head_up.png').convert_alpha()
    SNEK_HEAD_DOWN = BaseWindowConfig.get_pygame().image.load('../../assets/body/head_down.png').convert_alpha()
    SNEK_HEAD_LEFT = BaseWindowConfig.get_pygame().image.load('../../assets/body/head_left.png').convert_alpha()
    SNEK_HEAD_RIGHT = BaseWindowConfig.get_pygame().image.load('../../assets/body/head_right.png').convert_alpha()

    SNEK_BODY_BEND_LEFT = BaseWindowConfig.get_pygame().image.load('../../assets/body/body_bl.png').convert_alpha()
    SNEK_BODY_BEND_RIGHT = BaseWindowConfig.get_pygame().image.load('../../assets/body/body_br.png').convert_alpha()
    SNEK_BODY_TILL_LEFT = BaseWindowConfig.get_pygame().image.load('../../assets/body/body_tl.png').convert_alpha()
    SNEK_BODY_TILL_RIGHT = BaseWindowConfig.get_pygame().image.load('../../assets/body/body_tr.png').convert_alpha()

    SNEK_BODY_HORIZONTAL = BaseWindowConfig.get_pygame().image.load('../../assets/body/body_horizontal.png').convert_alpha()
    SNEK_BODY_VERTICAL = BaseWindowConfig.get_pygame().image.load('../../assets/body/body_vertical.png').convert_alpha()

    @staticmethod
    def get_font():
        return BaseWindowConfig.get_pygame().font.Font('../../assets/font/PressStart2P-Regular.ttf', 45)

from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HEART, HEART_TYPE

class Heart(PowerUp):
    def __init__ (self):
        super(). __init__(HEART, HEART_TYPE)

    def update(self):
        if game_speed >= 500:
            game_speed -= Score

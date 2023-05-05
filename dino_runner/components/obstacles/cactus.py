import random

from dino_runner.components.obstacles.obstacles import Obstacles
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class Cactus(Obstacles):
    CACTUS_TYPES = [
        (SMALL_CACTUS, 325),
        (LARGE_CACTUS, 300)
        
    ]

    def __init__(self):
        images, pos_y = random.choice(self.CACTUS_TYPES)
        cactus_images = random.choice(images)
        super().__init__(cactus_images, type)
        self.rect.y = pos_y

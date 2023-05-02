import random

from dino_runner.components.obstacles.obstacles import Obstacle

class Cactus(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        self.rect.y = 325

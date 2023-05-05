import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game_speed, player, on_deadth):
        if len(self.obstacles) == 0:
            obstacle = random.randint(0, 1)
            if obstacle == 0:
                self.obstacles.append(Cactus())
            else:
                self.obstacles.append(Bird(BIRD))
                
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
              on_deadth()

    def draw(self, screen):
        for obstacles in self.obstacles:
            obstacles.draw(screen)

    def reset(self):
        self.obsatcles = []


import pygame
import random
from dino_runner.components.obstacles.obstacles import Obstacles
from dino_runner.utils.constants import BIRD

class Bird(Obstacles):
    POS_Y_BIRD = 250
    def __init__(self, image):
        self.type = 0
        super().__init__(image[0], self.type)
        self.rect.y = self.POS_Y_BIRD
        self.step = 0
        
    def draw(self, screen):
        if self.step >= 10:
           self.step = 0
        self.image = BIRD[0] if self.step < 5 else BIRD[1]
        self.step +=1
        screen.blit(self.image, self.rect)
    

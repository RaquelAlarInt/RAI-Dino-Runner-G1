import pygame


class Collide:
    def __init__(self):
        self.collide = 0

    def update(self,game):
        self.collide += 1
        if self.collide == 1
            self.collide = +1

    def draw (self, screen):
        font = pygame.font.Font('freesansbold.ttf', 22)
        text = font.render(f"Collide: {self.collide}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 100)
        screen.blit(text, text_rect)
################
# Talha Mukhtar
# bullets
################

import pygame
from constants import *
from circleshape import CircleShape

class Bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

################
# Talha Mukhtar
# asteroid
################

import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time
    
    def split_or_die(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_off_angle = random.uniform(20, 50)
        baby_ast_1 = Asteroid(
                self.position.x,
                self.position.y,
                self.radius - ASTEROID_MIN_RADIUS
                )
        baby_ast_2 = Asteroid(
                self.position.x,
                self.position.y,
                self.radius - ASTEROID_MIN_RADIUS
                )
        baby_ast_1.velocity = self.velocity.rotate(split_off_angle) * 1.2
        baby_ast_2.velocity = self.velocity.rotate(-split_off_angle) * 1.2


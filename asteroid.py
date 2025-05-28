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
        self.durability = 5

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
                self.position.x + ASTEROID_MAX_RADIUS/2,
                self.position.y,
                self.radius - ASTEROID_MIN_RADIUS
                )
        baby_ast_2 = Asteroid(
                self.position.x,
                self.position.y + ASTEROID_MAX_RADIUS/2,
                self.radius - ASTEROID_MIN_RADIUS
                )
        baby_ast_1.velocity = self.velocity.rotate(split_off_angle) * 1.2
        baby_ast_2.velocity = self.velocity.rotate(-split_off_angle) * 1.2

    def asteroid_impact(self, other):
        self.durability -= 1
        other.durability -= 1
        if self.durability <= 0:
            self.split_or_die()
        if other.durability <= 0:
            other.split_or_die()

        impact_angle = random.uniform(30, 60)
        self.velocity.rotate(impact_angle)
        other.velocity.rotate(-impact_angle)


################
# Talha Mukhtar
# player
################

import pygame
from circleshape import CircleShape
from constants import *
from bullets import Bullet

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time):
        self.shot_timer -= delta_time
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_a]:
            self.rotate(delta_time * -1)
        if keys[pygame.K_w]:
            self.position += forward * PLAYER_SPEED * delta_time
        if keys[pygame.K_s]:
            self.position += forward * PLAYER_SPEED * delta_time * -1
        if keys[pygame.K_SPACE]:
            self.fire_bullet()

    def fire_bullet(self):
        if self.shot_timer <= 0:
            bullet = Bullet(self.position.x, self.position.y)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN

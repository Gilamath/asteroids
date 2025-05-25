################
# Talha Mukhtar
# main
################

import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField     # generates Asteroid objects

def main():
    ### initialization ###
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    fps_clock = pygame.time.Clock()
    dt = 0
    fps = 120                               # possible to change this FPS as a future setting?

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    ### game loop ###
    while True:
        for event in pygame.event.get():    # event loop; makes window's close button work
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updateable.update(dt)               # update all positions of objects
        for drawn_object in drawable:
            drawn_object.draw(screen)       # draw applicable objects on the screen
        for a in asteroids:
            if a.is_colliding_with(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()               # display update; call last
        dt = fps_clock.tick(fps) / 1000

if __name__ == "__main__":
    main()

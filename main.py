################
# Talha Mukhtar
# main
################

import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = updateable, drawable, asteroids)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    fps_clock = pygame.time.Clock()
    dt = 0
    fps = 120                               # possible to change this FPS as a future setting?

    while True:
        for event in pygame.event.get():    # event loop; makes window's close button work
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updateable.update(dt)               # update all positions of objects
        for drawn_object in drawable:
            drawn_object.draw(screen)       # draw applicable objects on the screen

        pygame.display.flip()               # display update; call last
        dt = fps_clock.tick(fps) / 1000

if __name__ == "__main__":
    main()

################
# Talha Mukhtar
# main
################

import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():    # event loop; makes window's close button work
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()   # display update; call last

if __name__ == "__main__":
    main()

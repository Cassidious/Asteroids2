import pygame
import sys
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
        

    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2)
    clock = pygame.time.Clock()
    asteroidfield = AsteroidField()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                asteroid.kill()
                player.kill()
                print("Game over!")
                sys.exit()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
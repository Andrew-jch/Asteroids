import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame_clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             return
            

        
        
        pygame.Surface.fill(screen, (0, 0, 0))
        updatable.update(dt)

        for instance in drawable:
           instance.draw(screen)

        for asteroid in asteroids:
           if asteroid.collision_check(player):
              print("Game over!")
              return
           
           for shot in shots:
              if asteroid.collision_check(shot):
                 shot.kill()
                 asteroid.split()

        pygame.display.flip()


        dt = pygame_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
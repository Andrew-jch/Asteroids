import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    pygame_clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

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

        pygame.display.flip()


        dt = pygame_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
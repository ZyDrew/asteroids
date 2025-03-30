import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #Init pygame
    pygame.init()

    #Init groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Init game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Initialize delta time and FPS
    clock = pygame.time.Clock()
    dt = 0

    #Initialize player
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Initialize asteroids
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Groups render
        updatable.update(dt)

        #Check collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
        
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()

        #Game render
        pygame.Surface.fill(screen, color=(0,0,0))
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        #Limit to 60 fps
        dt = clock.tick(60) / 1000
    #end while

#end main()

if __name__ == "__main__":
    main()
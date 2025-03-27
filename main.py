import pygame
from constants import *
from player import Player

def main():
    #Init pygame
    pygame.init()

    #Init groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    #Init game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Initialize delta time and FPS
    clock = pygame.time.Clock()
    dt = 0

    #Initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #Groups render
        updatable.update(dt)

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
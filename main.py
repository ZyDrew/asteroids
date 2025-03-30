import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #Init pygame
    pygame.init()

    #Init music
    pygame.mixer.music.load("./music/game-playback.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

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

    #Initialize game state
    score = 0
    start_chrono = pygame.time.get_ticks()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.unload()
                return
        
        #Groups render
        updatable.update(dt)

        #Check collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                draw_game_over(screen)
                pygame.mixer.music.unload()
                return
        
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
                    score += 1

        asteroid_list = asteroids.sprites()
        for i in range(0, len(asteroid_list)):
            for j in range(i+1, len(asteroid_list)):
                if asteroid_list[i].collision(asteroid_list[j]):
                    v1 = asteroid_list[i].velocity
                    v2 = asteroid_list[j].velocity

                    asteroid_list[i].velocity = v2
                    asteroid_list[j].velocity = v1

        #Game render
        pygame.Surface.fill(screen, "black")

        #Score
        font = pygame.font.SysFont("arial", 20)
        score_text = font.render(f"Score : {score}", True, "white")
        screen.blit(score_text, (SCREEN_WIDTH - 100, 10))

        #Chrono
        time_elapsed = pygame.time.get_ticks() - start_chrono
        total_seconds = time_elapsed // 1000  #Total in seconds
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        chrono_text = font.render(f"{minutes:02d}:{seconds:02d}", True, "white")
        screen.blit(chrono_text, (10, 10))

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        #end Game render

        #Limit to 60 fps
        dt = clock.tick(60) / 1000
    #end while

#end main()

def draw_game_over(screen):
    pygame.Surface.fill(screen, "black")
    font = pygame.font.SysFont("arial", 40)
    gameover_text = font.render("Game Over!", True, "white")
    quit_text = font.render("Press space key to exit...", True, "white")
    screen.blit(gameover_text, (SCREEN_WIDTH/2 - gameover_text.get_width()/2, SCREEN_HEIGHT/2 - gameover_text.get_height()/2))
    screen.blit(quit_text, (SCREEN_WIDTH/2 - quit_text.get_width()/2, SCREEN_HEIGHT/1.8 - quit_text.get_height()/1.8))
    pygame.display.flip()

    while(True):
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                return
        
        if keys[pygame.K_SPACE]:
            return
    #end while

#end draw_game_over

if __name__ == "__main__":
    main()
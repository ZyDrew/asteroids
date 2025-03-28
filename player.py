from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #override draw
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            (255,255,255),
            self.triangle(),
            2
        )
    
    #Rotating the player : left arrow key - right arrow key
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Left = Q key
        if keys[pygame.K_q]:
            self.rotate(-dt)
        
        # Right = D key
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Up = Z key
        if keys[pygame.K_z]:
            self.move(dt)
        
        # Down = S key
        if keys[pygame.K_s]:
            self.move(-dt)
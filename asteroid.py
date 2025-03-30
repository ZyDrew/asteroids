from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        new_asteroid_v1 = self.velocity.rotate(random_angle)
        new_asteroid_v2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Code for spliting without triggering the collision
        # If radius = 20 , we separate the 2 new asteroids with a lesser distance otherwise for medium asteroid >
        if new_radius == 20:
            distance = 18
        else:
            distance = 33

        new_asteroid = Asteroid(self.position.x+distance, self.position.y+distance, new_radius)
        new_asteroid_2 = Asteroid(self.position.x-distance, self.position.y-distance, new_radius)
        new_asteroid.velocity = new_asteroid_v1 * 1.2
        new_asteroid_2.velocity = new_asteroid_v2 * 1.2

    
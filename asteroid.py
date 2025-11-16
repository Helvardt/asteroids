import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position  += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_vector = self.velocity.rotate(random_angle)
        second_vector = self.velocity.rotate(-random_angle)
        self.radius -= ASTEROID_MIN_RADIUS
        first_Asteroid = Asteroid(self.position.x, self.position.y, self.radius) 
        second_Asteroid = Asteroid(self.position.x, self.position.y, self.radius) 
        first_Asteroid.velocity = new_vector * 1.2
        second_Asteroid.velocity = second_vector * 1.2
        
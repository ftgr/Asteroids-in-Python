import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        event = log_event("asteroid_split")
        random_num = random.uniform(20, 50)
        asteroid1_movement = self.velocity.rotate(random_num)
        asteroid2_movement = self.velocity.rotate(-random_num)
        asteroid1_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid2_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, asteroid1_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, asteroid2_radius)
        asteroid1.velocity = asteroid1_movement * 1.2
        asteroid2.velocity = asteroid2_movement * 1.2
              

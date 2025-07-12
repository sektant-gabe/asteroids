import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screem):
        pygame.draw.circle(screem, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_angle = self.velocity.rotate(random_angle)
            new_neg_angle = self.velocity.rotate(random_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            frst_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            scnd_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            frst_asteroid.velocity = new_angle * 1.2
            scnd_asteroid.velocity = new_neg_angle * 1.2

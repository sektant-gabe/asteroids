import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screem):
        pygame.draw.circle(screem, ASTEROID_COLOR, self.position, self.radius, ASTEROID_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE)
            new_angle = self.velocity.rotate(random_angle)
            new_neg_angle = self.velocity.rotate(random_angle * -1)
            frst_asteroid = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            scnd_asteroid = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            frst_asteroid.velocity = new_angle * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
            scnd_asteroid.velocity = new_neg_angle * ASTEROID_SPLIT_VELOCITY_MULTIPLIER

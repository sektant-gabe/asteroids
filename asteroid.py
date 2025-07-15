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
        self.velocity = pygame.Vector2(self.velocity.x * ASTEROID_ACCEL, self.velocity.y * ASTEROID_ACCEL)
        self.position += (self.velocity * ASTEROID_ACCEL) * dt
        if self.position.x > SCREEN_WIDTH + self.radius:
                self.position.x = 0 - self.radius
        if self.position.x < 0 - self.radius:
                self.position.x = SCREEN_WIDTH + self.radius
        if self.position.y > SCREEN_HEIGHT + self.radius:
                self.position.y = 0 - self.radius
        if self.position.y < 0 - self.radius:
                self.position.y = SCREEN_HEIGHT + self.radius



    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE)
        new_angle = self.velocity.rotate(random_angle)
        new_neg_angle = self.velocity.rotate(random_angle * -1)
        frst_asteroid = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        scnd_asteroid = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        frst_asteroid.velocity = new_angle * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        scnd_asteroid.velocity = new_neg_angle * ASTEROID_SPLIT_VELOCITY_MULTIPLIER

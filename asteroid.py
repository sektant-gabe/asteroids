import pygame
import random
import math
from circleshape import CircleShape
from constants import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.vertices = []
        self.speed = random.uniform(1, (40 - self.radius) * 4 / 15)
        self.dir = random.randrange(0, 360) * math.pi / 180

        # Make random asteroid sprites
        full_circle = random.uniform(18, 36)
        dist = random.uniform(self.radius / 2, self.radius)
        self.vertices = []
        while full_circle < 360:
            self.vertices.append([dist, full_circle])
            dist = random.uniform(self.radius / 2, self.radius)
            full_circle += random.uniform(18, 36)

    def draw(self, screem):
        for v in range(len(self.vertices)):
            if v == len(self.vertices) - 1:
                next_v = self.vertices[0]
            else:
                next_v = self.vertices[v + 1]
            this_v = self.vertices[v]
            pygame.draw.aaline(
                screem,
                ASTEROID_COLOR,
                (
                    self.position.x + this_v[0] * math.cos(this_v[1] * math.pi / 180),
                    self.position.y + this_v[0] * math.sin(this_v[1] * math.pi / 180)
                ),
                (
                    self.position.x + next_v[0] * math.cos(next_v[1] * math.pi / 180),
                    self.position.y + next_v[0] * math.sin(next_v[1] * math.pi / 180)
                ),
                ASTEROID_WIDTH
            )

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

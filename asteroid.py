import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screem):
        pygame.draw.circle(screem, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

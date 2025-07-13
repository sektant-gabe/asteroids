import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screem):
        pygame.draw.circle(screem, PLAYER_SHOT_COLOR, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

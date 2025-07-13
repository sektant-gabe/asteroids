import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, unity_type):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.shot_timer = 0
        self.damage_timer = 0
        self.radius = radius
        self.hp = hp

    def draw(self, screem):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def is_colliding(self, hitbox):
        return (self.position.distance_to(hitbox.position) <= self.radius + hitbox.radius)

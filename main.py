import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    digital_timer = 0

    while not player.is_dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(SCREEN_BACKGROUND_COLOR)
        updatable.update(digital_timer)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                player.take_damage(ASTEROID_DMG)

            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        digital_timer = clock.tick(DIGITAL_TIMER) / 1000


if __name__ == "__main__":
    main()

import pygame
import sys
import pygame_gui

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menu import Menu

pygame.init()
pygame.font.init()
game_font = pygame.font.SysFont(UI_FONT, UI_FONT_SIZE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def get_username():
    while True:
        digital_timer = clock.tick(DIGITAL_TIMER) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            MANAGER.process_events(event)

        MANAGER.update(digital_timer)

        screen.fill(SCREEN_BACKGROUND_COLOR)

        MANAGER.draw_ui(screen)

        pygame.display.update()

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Menu.containers = (drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    main_menu = Menu()
    digital_timer = 0
    asteroidfield = AsteroidField()


    while player.is_alive:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(SCREEN_BACKGROUND_COLOR)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                player.take_damage(ASTEROID_DMG)

            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()
                    player.score += 1

        for object in drawable:
            object.draw(screen)

        updatable.update(digital_timer)
        # score = game_font.render(str(player.score), False, TEXT_UI_PRIMARY_COLOR)
        # screen.blit(score, (0,0))
        pygame.display.flip()

        # limit the framerate to 60 FPS
        digital_timer = clock.tick(DIGITAL_TIMER) / 1000
    # If we broke out of the main loop, this means the player is dead
    # menu.draw_menu(screen , f"Your score was <<{player.score}>>! Better luck next time!")
    with open("scores.txt", "a") as score_file:
        score_file.write(f"\n{username},{player.score}")



if __name__ == "__main__":
    main()

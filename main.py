import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from button import Button
from menu import Menu

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def get_username():
    while True:
        digital_timer = clock.tick(DIGITAL_TIMER) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill(SCREEN_BACKGROUND_COLOR)

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(OPTIONS_BG_COLOR)

        OPTIONS_TEXT = get_font(UI_FONT_SIZE).render("This is the OPTIONS screen.", True, TEXT_UI_PRIMARY_COLOR)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(UI_FONT_SIZE).render("MAIN MENU", True, MENU_H1_COLOR)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=PLAY_RECT_IMG, pos=(640, 250), text_input="PLAY", font=get_font(45), base_color=BUTTON_BASE_COLOR, hovering_color=BUTTON_HOVERING_COLOR)
        OPTIONS_BUTTON = Button(image=PLAY_RECT_IMG, pos=(640, 250), text_input="OPTIONS", font=get_font(45), base_color=BUTTON_BASE_COLOR, hovering_color=BUTTON_HOVERING_COLOR)
        QUIT_BUTTON = Button(image=PLAY_RECT_IMG, pos=(640, 250), text_input="OPTIONS", font=get_font(45), base_color=BUTTON_BASE_COLOR, hovering_color=BUTTON_HOVERING_COLOR)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    options()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()

        pygame.display.update()

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main():
    pygame.init()
    pygame.font.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Menu")
    DT = 0
    BG = BG_IMG_PATH
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
            object.draw(SCREEN)

        updatable.update(DT)
        score = game_font.render(str(player.score), False, TEXT_UI_PRIMARY_COLOR)
        screen.blit(score, (0,0))
        pygame.display.flip()

        # limit the framerate to 60 FPS
        DT = clock.tick(DIGITAL_TIMER) / 1000
    # If we broke out of the main loop, this means the player is dead
    print(f"Your score was <<{player.score}>>! Better luck next time!")
    with open("scores.txt", "a") as score_file:
        score_file.write(f"\n{username},{player.score}")

    main_menu()


if __name__ == "__main__":
    main_menu()

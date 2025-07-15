import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from button import Button
from menu import Menu

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load(BG_IMG_PATH).convert()

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def game_loop():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    CLOCK = pygame.time.Clock()
    DT = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(BG, (0, 0))

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                player.take_damage(ASTEROID_DMG)
                if not player.is_alive:
                    game_over()

            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()
                    player.score += 1

        for object in drawable:
            object.draw(SCREEN)

        updatable.update(DT)
        score = get_font(40).render(str(player.score), False, TEXT_UI_PRIMARY_COLOR)
        SCREEN.blit(score, (0,0))

        # limit the framerate to 60 FPS
        DT = CLOCK.tick(60) / 1000
        pygame.display.update()
        pygame.display.flip()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(UI_FONT_SIZE).render("This is the OPTIONS screen.", True, TEXT_UI_PRIMARY_COLOR)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 260),
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

        MENU_TEXT = get_font(95).render("ASTEROID DOS CRIAS", True, MENU_H1_COLOR)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        FOOTER_TEXT = get_font(30).render("Ento'wn Thouma Productions LTDA", True, MENU_H1_COLOR)
        FOOTER_RECT = MENU_TEXT.get_rect(center=(800, 700))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(FOOTER_TEXT, FOOTER_RECT)

        PLAY_BUTTON = Button(image=None, pos=(640, 300), text_input="PLAY", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 375), text_input="OPTIONS", font=get_font(75), base_color="White", hovering_color="Blue")
        QUIT_BUTTON = Button(image=None, pos=(640, 450), text_input="QUIT", font=get_font(75), base_color="White", hovering_color="Red")


        for button in [PLAY_BUTTON,OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def game_over():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        TEXT = get_font(85).render("GAME OVER", True, "Red")
        RECT = TEXT.get_rect(center=(640, 170))
        SCREEN.blit(TEXT, RECT)

        BUTTON_1 = Button(image=None, pos=(640, 300), text_input="GO TO MAIN MENU", font=get_font(45), base_color="White", hovering_color="Green")
        BUTTON_1.changeColor(MOUSE_POS)
        BUTTON_1.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTON_1.checkForInput(MOUSE_POS):
                    main_menu()

        pygame.display.update()

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        TEXT = get_font(95).render("MISSAO:", True, "White")
        RECT = TEXT.get_rect(center=(640, 110))
        PLAY_TEXT = get_font(45).render("Purificar o espaco das outras formas geometricas", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 180))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_GAME = Button(image=None, pos=(640, 300), text_input="PLAY", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK = Button(image=None, pos=(640, 375), text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")

        PLAY_GAME.changeColor(PLAY_MOUSE_POS)
        PLAY_GAME.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_GAME.checkForInput(PLAY_MOUSE_POS):
                    game_loop()

                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

main_menu()

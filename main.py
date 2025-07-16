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
pygame.font.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
MOUSE_POS = pygame.mouse.get_pos()
pygame.display.set_caption("Menu")

BG = pygame.image.load(BG_IMG_PATH).convert()
UPDATABLE = pygame.sprite.Group()
DRAWABLE = pygame.sprite.Group()
ASTEROIDS = pygame.sprite.Group()
SHOTS = pygame.sprite.Group()
Player.containers = (UPDATABLE, DRAWABLE)
Asteroid.containers = (ASTEROIDS, UPDATABLE, DRAWABLE)
AsteroidField.containers = (UPDATABLE)
Shot.containers = (SHOTS, UPDATABLE, DRAWABLE)
PLAYER = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(145).render("ASTEROID DOS CRIAS", True, TITLE_COLOR)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 120))
        FOOTER_TEXT = get_font(30).render("Ento'wn Thouma Productions LTDA", True, TEXT_UI_PRIMARY_COLOR)
        FOOTER_RECT = FOOTER_TEXT.get_rect(center=(640, 680))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(FOOTER_TEXT, FOOTER_RECT)

        PLAY_BUTTON = Button(image=None, pos=(640, 350), text_input="PLAY", font=get_font(105), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_H1_COLOR)
        LEADERBOARD_BUTTON = Button(image=None, pos=(640, 435), text_input="LEADERBOARD", font=get_font(55), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_H1_COLOR)
        QUIT_BUTTON = Button(image=None, pos=(640, 580), text_input="QUIT", font=get_font(35), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_BACK_COLOR)

        for button in [PLAY_BUTTON,LEADERBOARD_BUTTON, QUIT_BUTTON]:
            button.update(SCREEN, MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    play()
                if LEADERBOARD_BUTTON.checkForInput(MOUSE_POS):
                    leaderboard()
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



def options():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(UI_FONT_SIZE).render("This is the OPTIONS screen.", True, TEXT_UI_PRIMARY_COLOR)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 260), text_input="BACK", font=get_font(75), base_color="Black", hovering_color=MENU_H1_COLOR)

        OPTIONS_BACK.changeColor(MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(MOUSE_POS):
                    main_menu()

        pygame.display.update()


def game_loop():
    MOUSE_POS = pygame.mouse.get_pos()
    DT = 0
    ASTEROIDFIELD = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(BG, (0, 0))

        for asteroid in ASTEROIDS:
            if PLAYER.is_colliding(asteroid):
                PLAYER.take_damage(ASTEROID_DMG)
                if not PLAYER.is_alive:
                    game_over()

            for shot in SHOTS:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()
                    PLAYER.score += 1

        for object in DRAWABLE:
            object.draw(SCREEN)

        UPDATABLE.update(DT)
        SCORE_TEXT = Button(image=None, pos=(640, 50), text_input="[ "+str(PLAYER.score)+" ]", font=get_font(35), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_H1_COLOR)
        SCORE_TEXT.update(SCREEN, MOUSE_POS)

        # limit the framerate to 60 FPS
        DT = CLOCK.tick(60) / 1000
        pygame.display.update()
        pygame.display.flip()


def game_over():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        GAMEOVER_TEXT = get_font(85).render("YOU DIED", True, MENU_BACK_COLOR)
        GAMEOVER_RECT = GAMEOVER_TEXT.get_rect(center=(640, 110))
        SCREEN.blit(GAMEOVER_TEXT, GAMEOVER_RECT)

        FINAL_SCORE_TEXT = get_font(65).render("Your final score is", True, TEXT_UI_PRIMARY_COLOR)
        FINAL_SCORE_RECT = FINAL_SCORE_TEXT.get_rect(center=(640, 250))
        SCREEN.blit(FINAL_SCORE_TEXT, FINAL_SCORE_RECT)

        SCORE_COUNT_TEXT = get_font(135).render(str(PLAYER.score), True, TEXT_UI_PRIMARY_COLOR)
        SCORE_COUNT_RECT = SCORE_COUNT_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(SCORE_COUNT_TEXT, SCORE_COUNT_RECT)

        BUTTON_1 = Button(image=None, pos=(640, 580), text_input="BACK", font=get_font(45), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_BACK_COLOR)
        BUTTON_1.update(SCREEN, MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTON_1.checkForInput(MOUSE_POS):
                    main_menu()

        pygame.display.update()

def leaderboard():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        TEXT = get_font(85).render("Oka's LEADERBOARD", True, TITLE_COLOR)
        RECT = TEXT.get_rect(center=(640, 110))
        SCREEN.blit(TEXT, RECT)

        BUTTON_1 = Button(image=None, pos=(640, 580), text_input="BACK", font=get_font(35), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_BACK_COLOR)
        BUTTON_1.update(SCREEN, MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTON_1.checkForInput(MOUSE_POS):
                    main_menu()

        pygame.display.update()

def play():
    USERNAME = ''
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        H1 = get_font(95).render("Type your username:", True, TEXT_UI_PRIMARY_COLOR)
        H1_RECT = H1.get_rect(center=(640, 110))
        SCREEN.blit(H1, H1_RECT)

        USERNAME_TEXT = Button(image=None, pos=(640, 210), text_input="[ "+USERNAME+" ]", font=get_font(55), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=TEXT_UI_PRIMARY_COLOR)
        USERNAME_TEXT.update(SCREEN, MOUSE_POS)

        if len(USERNAME) > 2:
            PLAY_GAME = Button(image=None, pos=(640, 350), text_input="START", font=get_font(95), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_H1_COLOR)
            PLAY_GAME.update(SCREEN, MOUSE_POS)

        PLAY_BACK = Button(image=None, pos=(640, 580), text_input="BACK", font=get_font(35), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_BACK_COLOR)
        PLAY_BACK.update(SCREEN, MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_GAME.checkForInput(MOUSE_POS):
                    PLAYER.username = USERNAME
                    game_loop()

                if PLAY_BACK.checkForInput(MOUSE_POS):
                    main_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    USERNAME = USERNAME[:-1]
                else:
                    if len(USERNAME) < 5:
                        USERNAME += event.unicode.upper()

        pygame.display.update()

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

main_menu()

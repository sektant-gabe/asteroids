import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from button import Button

pygame.init()
pygame.font.init()
pygame.mixer.init()

asteroid_death_sound = pygame.mixer.Sound(ASTEROID_DEATH_SOUND)
asteroid_death_sound.set_volume(0.25)
button_click_sound = pygame.mixer.Sound(UI_CLICK_SOUND)
type_sound = pygame.mixer.Sound(TYPE_SOUND)
delete_sound = pygame.mixer.Sound(HIT2_SOUND)
player_shot_sound = pygame.mixer.Sound(HIT1_SOUND)
player_shot_sound.set_volume(0.4)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
MOUSE_POS = pygame.mouse.get_pos()
pygame.display.set_caption("Menu")
UPDATABLE = pygame.sprite.Group()
DRAWABLE = pygame.sprite.Group()
ASTEROIDS = pygame.sprite.Group()
SHOTS = pygame.sprite.Group()
Player.containers = (UPDATABLE, DRAWABLE)
Asteroid.containers = (ASTEROIDS, UPDATABLE, DRAWABLE)
AsteroidField.containers = UPDATABLE
Shot.containers = (SHOTS, UPDATABLE, DRAWABLE)
BG = pygame.image.load(BG_IMG_PATH).convert()
PLAYER = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
ASTEROID_SPAWNER = AsteroidField()

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG)

        mouse_pos = pygame.mouse.get_pos()

        draw_text("ASTEROID DOS CRIAS", TITLE_FONT_SIZE, TITLE_COLOR, SCREEN_MIDDLE_X, 120)
        draw_text("Ento'wn Thouma Productions LTDA", FOOTER_FONT_SIZE, TEXT_UI_PRIMARY_COLOR, SCREEN_MIDDLE_X, 680)

        play_button = Button(image=None, pos=(SCREEN_MIDDLE_X, 350), text_input="PLAY", font=get_font(105), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_H1_COLOR)
        leaderboard_button = Button(image=None, pos=(SCREEN_MIDDLE_X, 435), text_input="LEADERBOARD", font=get_font(55), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_H1_COLOR)
        quit_button = Button(image=None, pos=(SCREEN_MIDDLE_X, 580), text_input="QUIT", font=get_font(35), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_BACK_COLOR)

        for button in [play_button,leaderboard_button, quit_button]:
            button.update(SCREEN, mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    button_click_sound.play()
                    play()
                if leaderboard_button.checkForInput(mouse_pos):
                    button_click_sound.play()
                    leaderboard()
                if quit_button.checkForInput(mouse_pos):
                    button_click_sound.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def game_loop():
    mouse_pos = pygame.mouse.get_pos()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(BG)

        for asteroid in ASTEROIDS:
            if PLAYER.is_colliding(asteroid):
                PLAYER.take_damage(ASTEROID_DMG)
                if not PLAYER.is_alive:
                    game_over()

            for shot in SHOTS:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    asteroid_death_sound.play()
                    shot.kill()
                    PLAYER.score += 1

        for drawable_object in DRAWABLE:
            drawable_object.draw(SCREEN)

        if PLAYER.score == 100 * ASTEROID_SPAWNER.current_wave:
            ASTEROID_SPAWNER.current_wave += 1

        UPDATABLE.update(dt)

        score_text = Button(image=None,
                            pos=(100, 65),
                            text_input="[ "+str(PLAYER.score)+" ]",
                            font=get_font(35),
                            base_color=TEXT_UI_PRIMARY_COLOR,
                            hovering_color=MENU_H1_COLOR)

        score_text.update(SCREEN, mouse_pos)

        player_hp_text = Button(image=None, pos=(1180, 65),
                                text_input="[ " + str(PLAYER.hp) + " ]",
                                font=get_font(35),
                                base_color=TEXT_UI_PRIMARY_COLOR,
                                hovering_color=MENU_H1_COLOR)

        player_hp_text.update(SCREEN, mouse_pos)

        wave_text = Button(image=None, pos=(SCREEN_MIDDLE_X, 65),
                                text_input="[ " + str(ASTEROID_SPAWNER.current_wave) + " ]",
                                font=get_font(35),
                                base_color=TEXT_UI_PRIMARY_COLOR,
                                hovering_color=MENU_H1_COLOR)

        wave_text.update(SCREEN, mouse_pos)

        # limit the framerate to 60 FPS
        dt = CLOCK.tick(60) / 1000
        pygame.display.update()
        pygame.display.flip()

def game_over():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.blit(BG)

        draw_text("YOU DIED", H1_FONT_SIZE, GAME_OVER_COLOR, SCREEN_MIDDLE_X, SCREEN_MIDDLE_TOP)
        draw_text("Your final score is", H3_FONT_SIZE, TEXT_UI_PRIMARY_COLOR, SCREEN_MIDDLE_X, SCREEN_MIDDLE_Y - 130)
        draw_text(str(PLAYER.score), H2_FONT_SIZE, FINAL_SCORE_COLOR, SCREEN_MIDDLE_X, SCREEN_MIDDLE_Y)

        back_button = Button(image=None, pos=(SCREEN_MIDDLE_X, SCREEN_MIDDLE_BOTTOM), text_input="BACK", font=get_font(BACK_BUTTON_SIZE), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_BACK_COLOR)
        back_button.update(SCREEN, mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    button_click_sound.play()
                    if PLAYER.username != "AAA":
                        with open("scores.txt", "a", encoding="UTF-8") as score_file:
                            score_file.write(f"{PLAYER.username},{PLAYER.score}\n")
                    main_menu()

        pygame.display.update()

def load_scores_file(file_path):
    scores = []
    with open(file_path) as f:
        for file_line in f:
            name, score_str = file_line.strip().split(',')
            scores.append([name, int(score_str)])
    scores.sort(key=lambda run: run[1], reverse=True)
    for i, (name, score) in enumerate(scores[:MAX_SCORES_DISPLAY]):
        y = 230 + SPACE_BETWEEN_SCORES * i
        draw_text(name, H4_FONT_SIZE - 5, SCORE_NAME_COLOR, SCREEN_MIDDLE_LEFT, y)
        draw_text(str(score), H4_FONT_SIZE - 5, SCORE_NAME_COLOR, SCREEN_MIDDLE_RIGHT, y)

def leaderboard():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.blit(BG)


        draw_text("Oka's Leaderboard", H1_FONT_SIZE, TEXT_UI_PRIMARY_COLOR, SCREEN_MIDDLE_X + 20, 110)

        load_scores_file(SCORES_FILE_PATH)

        back_button = Button(
                             image=None,
                             pos=(SCREEN_MIDDLE_X, SCREEN_MIDDLE_BOTTOM),
                             text_input="BACK",
                             font=get_font(BACK_BUTTON_SIZE),
                             base_color=TEXT_UI_PRIMARY_COLOR,
                             hovering_color=MENU_BACK_COLOR
                             )

        back_button.update(SCREEN, mouse_pos)

        for leaderboard_event in pygame.event.get():
            if leaderboard_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if leaderboard_event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    button_click_sound.play()
                    main_menu()

        pygame.display.update()

def play():
    current_username = ''
    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.blit(BG)

        draw_text("Type your username...", H2_FONT_SIZE, TEXT_UI_PRIMARY_COLOR, SCREEN_MIDDLE_X, SCREEN_MIDDLE_TOP)

        username_text = Button(image=None,
                               pos=(SCREEN_MIDDLE_X, 210),
                               text_input="[ "+current_username+" ]",
                               font=get_font(55),
                               base_color=TEXT_UI_PRIMARY_COLOR,
                               hovering_color=TEXT_UI_PRIMARY_COLOR)

        username_text.update(SCREEN, mouse_pos)



        play_button = Button(image=None,
                            pos=(SCREEN_MIDDLE_X, SCREEN_MIDDLE_Y),
                            text_input="START",
                            font=get_font(95),
                            base_color=TEXT_UI_PRIMARY_COLOR,
                            hovering_color=MENU_H1_COLOR,
                            is_inactive=True)
        if len(current_username) > 2:
           play_button.is_inactive = False

        play_button.update(SCREEN, mouse_pos)

        back_button = Button(image=None, pos=(SCREEN_MIDDLE_X, SCREEN_MIDDLE_BOTTOM), text_input="BACK", font=get_font(BACK_BUTTON_SIZE), base_color=TEXT_UI_PRIMARY_COLOR, hovering_color=MENU_BACK_COLOR)
        back_button.update(SCREEN, mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(current_username) > 2 and play_button is not None:
                    if play_button.checkForInput(mouse_pos):
                        PLAYER.username = current_username
                        button_click_sound.play()
                        game_loop()

                if back_button.checkForInput(mouse_pos):
                    button_click_sound.play()
                    main_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    current_username = current_username[:-1]
                    delete_sound.play()

                else:
                    if len(current_username) < 8:
                        current_username += event.unicode.upper()
                        type_sound.play()

        pygame.display.update()

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def draw_text(text, font_size, color, x, y):
    text = get_font(font_size).render(text, True, color)
    rect = text.get_rect(center=(x, y))
    SCREEN.blit(text, rect)

main_menu()

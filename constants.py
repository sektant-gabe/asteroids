# constants.py
# === Tela ===
SCREEN_WIDTH               = 1280
SCREEN_HEIGHT              = 720
SCREEN_MIDDLE_X            = SCREEN_WIDTH / 2
SCREEN_MIDDLE_Y            = SCREEN_HEIGHT / 2
SCREEN_MIDDLE_TOP          = SCREEN_MIDDLE_Y * 0.25
SCREEN_MIDDLE_BOTTOM       = SCREEN_MIDDLE_Y * 1.75
SCREEN_MIDDLE_LEFT         = SCREEN_MIDDLE_X * 0.45
SCREEN_MIDDLE_RIGHT        = SCREEN_MIDDLE_X * 1.65
BG_IMG_PATH                = "assets/bg.png"
SCREEN_BACKGROUND_COLOR    = "black"
HIT1_SOUND                 = 'assets/hit3.wav'
HIT2_SOUND                 = 'assets/hit2.wav'
HIT3_SOUND                 = 'assets/hit3.wav'
HIT4_SOUND                 = 'assets/hit4.wav'
TYPE_SOUND                 = 'assets/hit4.wav'
UI_HOVER_SOUND             = 'assets/hit3.wav'
UI_CLICK_SOUND             = 'assets/hit2.wav'
ASTEROID_SPLIT_SOUND       = 'assets/asteroid_split.wav'
ASTEROID_DEATH_SOUND       = 'assets/type.wav'

# === UI / Menu / Timer ===
UI_FONT                    = 'RuneScape UF'
UI_FONT_SIZE               = 40
SPACE_BETWEEN_SCORES       = 45
MAX_SCORES_DISPLAY         = 8
SCORES_FILE_PATH           = "scores.txt"
SCORE_NAME_COLOR           = "#FAEB92"
BACK_BUTTON_SIZE           = 45
TITLE_FONT_SIZE            = 145
FOOTER_FONT_SIZE           = 35
H1_FONT_SIZE               = 120
H2_FONT_SIZE               = 100
H3_FONT_SIZE               = 80
H4_FONT_SIZE               = 60
UI_INPUT_WIDTH             = 400
UI_INPUT_X                 = 50
UI_INPUT_Y                 = 50
TEXT_UI_PRIMARY_COLOR      = "#FAEB92"
TITLE_COLOR                = "Purple"
GAME_OVER_COLOR            = "Red"
FINAL_SCORE_COLOR          = "green"
MENU_BG_COLOR              = (0, 0, 0)
MENU_H1_COLOR              = '#CC66DA'
MENU_BACK_COLOR            = '#CC66DA'
OPTIONS_BG_COLOR           = "black"
BUTTON_BASE_COLOR          = "Green"
BUTTON_HOVERING_COLOR      = (255, 255, 255)
SCORE_COUNT_COLOR          = ''
DIGITAL_TIMER              = 60

# === Jogador ===
PLAYER_HP: int             = 5
PLAYER_WIDTH               = 0
PLAYER_RADIUS              = 20
PLAYER_SPEED               = 300
PLAYER_TURN_SPEED          = 300
PLAYER_SHOOT_SPEED         = 600
PLAYER_SHOOT_COOLDOWN      = 0.11
PLAYER_DMG_COOLDOWN        = 2.5
PLAYER_COLOR               = "#FAEB92"
PLAYER_SHOT_COLOR          = "#FAEB92"
PLAYER_SHOT_WIDTH          = 2
PLAYER_DMG_COLOR           = "#CC66DA"
PLAYER_DMG_COOLDOWN_COLOR  = "#CC66DA"

# === Asteroides ===
ASTEROID_WIDTH                         = 5
ASTEROID_ACCEL: float                  = 1.0002
ASTEROID_DMG                           = 1
ASTEROID_KINDS                         = 4
ASTEROID_MIN_RADIUS                    = 25
ASTEROID_MAX_RADIUS                    = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_MIN_SPEED                     = 50
ASTEROID_MAX_SPEED                     = 130
ASTEROID_SPAWN_RATE                    = 1.5
ASTEROID_LIFE_TIMER                    = 3000 # frames
ASTEROID_SHOT_COOLDOWN                 = 0.8
ASTEROID_SPLIT_VELOCITY_MULTIPLIER     = 1.12
ASTEROID_MIN_SPLIT_ANGLE               = 20
ASTEROID_MAX_SPLIT_ANGLE               = 40
ASTEROID_MIN_SPAWN_ANGLE               = -30
ASTEROID_MAX_SPAWN_ANGLE               = 30
ASTEROID_COLOR                         = "#FAEB92"

# === Elite ===
IS_ELITE               = False
ELITE_HP_MULTIPLIER    = 1.3
ELITE_DMG_MULTIPLIER   = 10

# === Chefes / Boss ===
RARE_RADIUS            = 80
LIEUTENANT_HP          = 25
LIEUTENANT_RADIUS      = 100
MINI_BOSS_HP           = 50
MINI_BOSS_RADIUS       = 120
BOSS_HP                = 100
BOSS_RADIUS            = 160

# === Armas (Weapon) ===
SHOT_RADIUS            = 5

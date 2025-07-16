# constants.py

# === Tela ===
SCREEN_WIDTH               = 1280
SCREEN_HEIGHT              = 720
BG_IMG_PATH                = "assets/bg.png"
SCREEN_BACKGROUND_COLOR    = "black"

# === UI / Menu / Timer ===
UI_FONT                    = 'RuneScape UF'
UI_FONT_SIZE               = 40
UI_INPUT_WIDTH             = 400
UI_INPUT_X                 = 50
UI_INPUT_Y                 = 50
TEXT_UI_PRIMARY_COLOR      = "#FAEB92"
TITLE_COLOR                = "Purple"
MENU_BG_COLOR              = (0, 0, 0)
MENU_H1_COLOR              = '#CC66DA'
MENU_BACK_COLOR            = '#CC66DA'
OPTIONS_BG_COLOR           = "black"
BUTTON_BASE_COLOR          = "Green"
BUTTON_HOVERING_COLOR      = (255, 255, 255)
SCORE_COUNT_COLOR          = ''
DIGITAL_TIMER              = 60

# === Jogador ===
PLAYER_HP                  = 3
PLAYER_WIDTH               = 5
PLAYER_RADIUS              = 20
PLAYER_SPEED               = 200
PLAYER_TURN_SPEED          = 300
PLAYER_SHOOT_SPEED         = 500
PLAYER_SHOOT_COOLDOWN      = 0.11
PLAYER_DMG_COOLDOWN        = 1.2
PLAYER_COLOR               = "#FAEB92"
PLAYER_SHOT_COLOR          = "#FAEB92"
PLAYER_SHOT_WIDTH          = 2
PLAYER_DMG_COLOR           = "#CC66DA"
PLAYER_DMG_COOLDOWN_COLOR  = "#CC66DA"

# === Asteroides ===
ASTEROID_WIDTH                         = 5
ASTEROID_ACCEL                         = 1.0002
ASTEROID_DMG                           = 1
ASTEROID_KINDS                         = 3
ASTEROID_MIN_RADIUS                    = 20
ASTEROID_MAX_RADIUS                    = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_MIN_SPEED                     = 40
ASTEROID_MAX_SPEED                     = 80
ASTEROID_SPAWN_RATE                    = 1.5    # segundos
ASTEROID_SHOT_COOLDOWN                 = 0.8
ASTEROID_SPLIT_VELOCITY_MULTIPLIER     = 1.2
ASTEROID_MIN_SPLIT_ANGLE               = 20
ASTEROID_MAX_SPLIT_ANGLE               = 50
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
SHOT_RADIUS            = 8

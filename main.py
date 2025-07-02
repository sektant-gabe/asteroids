import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
digital_timer = 0

# sets player position to be on the middle of the screen
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_img = pygame.image.load("player_img.png")
player_color = (0, 128, 255) # Blue
# polygon_shape = [(-20, -20), (20, -20), (0, 30)] # Example triangle


while running:
# poll for events
# pygame.QUIT event means the user clicked X to close your WindowsError
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * digital_timer
    if keys[pygame.K_s]:
        player_pos.y += 300 * digital_timer
    if keys[pygame.K_a]:
        player_pos.x -= 300 * digital_timer
    if keys[pygame.K_d]:
        player_pos.x += 300 * digital_timer


    digital_timer = clock.tick(60) / 1000 # limits fps to 60 and splits into miliseconds

    # if player_pos.x >= 1260:
    #     player_pos.x = 1260
    # if player_pos.x <= 20:
    #     player_pos.x = 20
    # if player_pos.y >= 700:
    #     player_pos.y = 700
    # if player_pos.y <= 20:
    #     player_pos.y = 20

    # draw to player
    pygame.draw.circle(screen, player_color, player_pos, 40)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()

import pygame
from constants import *

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.font = pygame.font.SysFont(UI_FONT, UI_FONT_SIZE)
        self.is_active = True
        self.position = pygame.Vector2((SCREEN_WIDTH / 2) - 200, (SCREEN_HEIGHT / 2) - 200)
        self.text = ''

    def draw(self, screen):
        if self.is_active:
            text_surface = self.font.render(self.text, True, TEXT_UI_PRIMARY_COLOR)
            screen.blit(text_surface, self.position)

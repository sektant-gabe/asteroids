class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, is_inactive=False):
        self.image = image
        self.position_x = pos[0]
        self.position_y = pos[1]
        self.font = font
        self.is_inactive = is_inactive
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.position_x, self.position_y))
        self.text_rect = self.text.get_rect(center=(self.position_x, self.position_y))


    def update(self, screen, mouse_position):
        if self.is_inactive:
            self.base_color = "Grey"
            self.hovering_color = "Grey"
        if mouse_position[0] in range(self.rect.left, self.rect.right) and mouse_position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and not self.is_inactive:
            return True
        return False

    # def changeColor(self, position):

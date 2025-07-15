import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.hp = PLAYER_HP
        self.speed = PLAYER_SPEED
        self.score = 0

    def draw(self, screem):
        if self.damage_timer > 0:
            pygame.draw.polygon(screem, PLAYER_DMG_COOLDOWN_COLOR, self.triangle(), PLAYER_WIDTH)
        else:
            pygame.draw.polygon(screem, PLAYER_COLOR, self.triangle(), PLAYER_WIDTH)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, digital_timer):
        self.rotation += PLAYER_TURN_SPEED * digital_timer

    def take_damage(self, damage):
        if not self.damage_timer > 0:
            print(f"\n...you took {damage} DMG...")
            self.hp -= damage
            print(f"...you now have {self.hp} HP remaining...")
            if self.hp <= 0:
                print('\nYou are dead!!!')
                pygame.exit()
            self.damage_timer = PLAYER_DMG_COOLDOWN



    def update(self, digital_timer):
            keys = pygame.key.get_pressed()
            self.shot_timer -= digital_timer
            self.damage_timer -= digital_timer

            # Screen edges as walls
            # if self.position.x + self.radius > WIDTH or self.position.x - self.radius < 0:
            #     self. *= -1
            # if self.position.y + self.radius > HEIGHT or self.position.y - self.radius < 0:
            #     self.speed_y *= -1

            # Screen edges as portals
            if self.position.x > SCREEN_WIDTH + self.radius:
                    self.position.x = 0 - self.radius
            if self.position.x < 0 - self.radius:
                    self.position.x = SCREEN_WIDTH + self.radius
            if self.position.y > SCREEN_HEIGHT + self.radius:
                    self.position.y = 0 - self.radius
            if self.position.y < 0 - self.radius:
                    self.position.y = SCREEN_HEIGHT + self.radius

            # Keybinds
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.rotate(digital_timer * -1)
            if keys[pygame.K_d]:
                self.rotate(digital_timer)
            if keys[pygame.K_s]:
                self.move(digital_timer * -1)
            if keys[pygame.K_w]:
                self.move(digital_timer)
            if keys[pygame.K_j]:
                self.shoot()


    def move(self, digital_timer):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * digital_timer

    def shoot(self):
        if not self.shot_timer > 0:
            shot = Shot(self.position[0], self.position[1])
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity *=  PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN

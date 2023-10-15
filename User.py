from mod import *
import random as rand

FRONT_IMAGE = pygame.image.load("Assets/virtaFront.png").convert_alpha()
BACK_IMAGE = pygame.image.load("Assets/virtaBack.png").convert_alpha()
PLAYER_FRONT_IMAGE = pygame.transform.scale(FRONT_IMAGE, (70, 85))
PLAYER_BACK_IMAGE = pygame.transform.scale(BACK_IMAGE, (70, 85))
SPEED = 5

class User(pygame.sprite.Sprite):
    moving = False
    def __init__(self, x, y):
        super().__init__()
        self.image = PLAYER_FRONT_IMAGE
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def movement(self):
        keys_pressed = pygame.key.get_pressed()
        self.moving = False
        if keys_pressed[pygame.K_a] and self.rect.x - SPEED > 0:
            self.rect.x -= SPEED
            self.moving = True
        if keys_pressed[pygame.K_d] and self.rect.x - SPEED + self.rect.width < WIDTH:
            self.rect.x += SPEED
            self.moving = True
        if keys_pressed[pygame.K_w] and self.rect.y - SPEED > 0:
            self.image = PLAYER_BACK_IMAGE
            self.rect.y -= SPEED
            self.moving = True
        if keys_pressed[pygame.K_s] and self.rect.y + SPEED + self.rect.height < HEIGHT:
            self.image = PLAYER_FRONT_IMAGE
            self.rect.y += SPEED
            self.moving = True

    # TODO - Jhon make an inventory to hold different critters and items
    def inventory(self):
        pass

    # TODO - TBD find a way to damage critters and make them vulnerable
    def attack(self, critter):
        pass

    def draw(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))

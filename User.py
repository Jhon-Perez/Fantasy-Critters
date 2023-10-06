from mod import *
import random as rand

IMAGE = pygame.image.load("Assets/stickman.png").convert_alpha()
PLAYER_IMAGE = pygame.transform.scale(IMAGE, (75, 100))
SPEED = 5

class User(pygame.sprite.Sprite):
    moving = False
    def __init__(self, x, y):
        super().__init__()
        self.image = PLAYER_IMAGE
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and self.rect.x - SPEED > 0:
            self.rect.x -= SPEED
            self.moving = True
        if keys_pressed[pygame.K_d] and self.rect.x - SPEED + self.rect.width < WIDTH:
            self.rect.x += SPEED
            self.moving = True
        if keys_pressed[pygame.K_w] and self.rect.y - SPEED > 0:
            self.rect.y -= SPEED
            self.moving = True
        if keys_pressed[pygame.K_s] and self.rect.y + SPEED + self.rect.height < HEIGHT:
            self.rect.y += SPEED
            self.moving = True

    def inventory(self):
        pass

    def draw(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))

import pygame
from mod import wn, WIDTH, HEIGHT

PLAYER_WIDTH = 70
PLAYER_HEIGHT = 85

FRONT_IMAGE = pygame.image.load("Assets/virtaFront.png").convert_alpha()
BACK_IMAGE = pygame.image.load("Assets/virtaBack.png").convert_alpha()
PLAYER_FRONT_IMAGE = pygame.transform.scale(FRONT_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_BACK_IMAGE = pygame.transform.scale(BACK_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
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

    def is_walking_on_grass(self, sprite_group):
        for sprite in sprite_group:
            pass

    # TODO - Jhon make an inventory to hold different critters and items
    def inventory(self):
        pass

    # TODO - TBD find a way to damage critters and make them vulnerable
    def attack(self, critter, move_selection):
        print(critter.health)
        if move_selection==1:
            critter.health-=25

        if move_selection==2:
            critter.health-=10

        if move_selection==3:
            critter.health-=10

        if move_selection==4:
            critter.health-=1000000000
            
        print(critter.health)

    def draw(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))

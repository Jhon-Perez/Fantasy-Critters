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
    score = 0
    # instead of self it is now Jhon because Jhon is cool (not really he is kinda lame tbh-Agreed)
    def __init__(Jhon, x, y, health):
        super().__init__()
        Jhon.image = PLAYER_FRONT_IMAGE
        Jhon.rect = Jhon.image.get_rect()
        Jhon.health = health

        Jhon.rect.x = x
        Jhon.rect.y = y

    def movement(Jhon):
        keys_pressed = pygame.key.get_pressed()
        Jhon.moving = False
        if keys_pressed[pygame.K_a] and Jhon.rect.x - SPEED > 0:
            Jhon.rect.x -= SPEED
            Jhon.moving = True
        if keys_pressed[pygame.K_d] and Jhon.rect.x - SPEED + Jhon.rect.width < WIDTH:
            Jhon.rect.x += SPEED
            Jhon.moving = True
        if keys_pressed[pygame.K_w] and Jhon.rect.y - SPEED > 0:
            Jhon.image = PLAYER_BACK_IMAGE
            Jhon.rect.y -= SPEED
            Jhon.moving = True
        if keys_pressed[pygame.K_s] and Jhon.rect.y + SPEED + Jhon.rect.height < HEIGHT:
            Jhon.image = PLAYER_FRONT_IMAGE
            Jhon.rect.y += SPEED
            Jhon.moving = True

    def attack(Jhon, critter, move_selection):
        print(critter.health)
        if move_selection == 1:
            critter.health -= 25
        elif move_selection == 2:
            critter.health -= 10
        elif move_selection == 3:
            critter.health -= 10
        elif move_selection == 4:
            critter.health -= 1000000000

        if critter.health > 0:
            Jhon.health -= critter.damage
            if Jhon.health < 0:
                Jhon.health = 0
        else:
            Jhon.score += critter.score
            
        print(critter.health)
        print(Jhon.health)

    def draw(Jhon):
        wn.blit(Jhon.image, (Jhon.rect.x, Jhon.rect.y))

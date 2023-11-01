import pygame
from mod import wn, WIDTH, HEIGHT, get_image

PLAYER_WIDTH = 73
PLAYER_HEIGHT = 100

SPEED = 5

# I wish you made the sprites the same distance away like a PROPER sprite sheet :)
PLAYER_IMAGE = pygame.image.load("Assets/Sprite_Sheet.png").convert_alpha()
animation_list = [
    [
        get_image(PLAYER_IMAGE, 50, 15, 0, PLAYER_WIDTH, PLAYER_HEIGHT),
        get_image(PLAYER_IMAGE, 145, 15, 1, PLAYER_WIDTH, PLAYER_HEIGHT),
        get_image(PLAYER_IMAGE, 240, 15, 2, PLAYER_WIDTH-5, PLAYER_HEIGHT),
        get_image(PLAYER_IMAGE, 320, 15, 3, PLAYER_WIDTH, PLAYER_HEIGHT),
    ],
    [
        get_image(PLAYER_IMAGE, 50, 115, 0, PLAYER_WIDTH, PLAYER_HEIGHT),
        get_image(PLAYER_IMAGE, 145, 115, 1, PLAYER_WIDTH, PLAYER_HEIGHT),
        get_image(PLAYER_IMAGE, 240, 115, 2, PLAYER_WIDTH-5, PLAYER_HEIGHT),
        get_image(PLAYER_IMAGE, 320, 115, 3, PLAYER_WIDTH, PLAYER_HEIGHT),
    ]
]

class User(pygame.sprite.Sprite):
    moving = False
    score = 0
    frame = 1
    last_update = pygame.time.get_ticks()
    def __init__(self, x, y, health):
        super().__init__()
        self.image = animation_list[0][0]
        self.rect = self.image.get_rect()
        self.health = health

        self.rect.x = x
        self.rect.y = y

    def movement(self, current_time, animation_cooldown):
        keys_pressed = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        self.moving = False
        if keys_pressed[pygame.K_a] and self.rect.x - SPEED > 0:
            self.image = animation_list[1][self.frame]
            if current_time - self.last_update > animation_cooldown:
                self.frame += 1
                self.last_update = current_time
                if self.frame >= 4:
                    self.frame = 1
            self.rect.x -= SPEED
            self.moving = True
        if keys_pressed[pygame.K_d] and self.rect.x - SPEED + self.rect.width < WIDTH:
            self.image = animation_list[0][self.frame]
            if current_time - self.last_update > animation_cooldown:
                self.frame += 1
                self.last_update = current_time
                if self.frame >= 4:
                    self.frame = 1
            self.rect.x += SPEED
            self.moving = True
        if keys_pressed[pygame.K_w] and self.rect.y - SPEED > 0:
            self.image = animation_list[1][0]
            self.rect.y -= SPEED
            self.moving = True
        if keys_pressed[pygame.K_s] and self.rect.y + SPEED + self.rect.height < HEIGHT:
            self.image = animation_list[0][0]
            self.rect.y += SPEED
            self.moving = True

    def attack(self, critter, move_selection):
        if move_selection == 1:
            critter.health -= 25
        elif move_selection == 2:
            critter.health -= 10
        elif move_selection == 3:
            critter.health -= 10
        elif move_selection == 4:
            critter.health -= 1000000000

        if critter.health > 0:
            self.health -= critter.damage
            if self.health < 0:
                self.health = 0
        else:
            self.score += critter.score

    def draw(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))

if __name__ == "__main__":
    import sys
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 60
    current_time = 0
    animation_cooldown = 250

    user = User(WIDTH/2, HEIGHT/2, 99999999)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        wn.fill((200, 255, 255))

        for i, row in enumerate(animation_list):
            for j, sprite in enumerate(row):
                wn.blit(sprite, (j * 90 + 5, 100 * i + 10))
    
        user.movement(current_time, animation_cooldown)
        user.draw()

        pygame.display.update()
        clock.tick(FPS)

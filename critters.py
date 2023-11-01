import pygame
from mod import wn, WIDTH, HEIGHT, get_image

CRITTERS = pygame.image.load("Assets/Sprite_Sheet.png").convert_alpha()

class Critter(pygame.sprite.Sprite):
    critter_list = [
        get_image(CRITTERS, 50, 230, 0, 125, 120),
        get_image(CRITTERS, 175, 230, 0, 100, 120),
        get_image(CRITTERS, 285, 220, 0, 125, 130),
        get_image(CRITTERS, 65, 360, 0, 90, 135),
        get_image(CRITTERS, 165, 355, 0, 150, 155),
        get_image(CRITTERS, 320, 390, 0, 95, 120),
    ]
    def __init__(self, index, health, damage, name, score, x = 625, y = 150):
        super().__init__()
        self.image = self.critter_list[index]
        self.rect = self.image.get_rect()

        self.health = health
        self.damage = damage
        self.name = name
        self.score = score

        self.rect.x = x
        self.rect.y = y

    def draw(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))
        
if __name__ == "__main__":
    import sys
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 60

    random_critter = Critter(4, 1, 1, "Frying Pan", 69)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        wn.fill((200, 255, 255))

        for i, critter in enumerate(random_critter.critter_list):
            wn.blit(critter, (i * 145 + 5, 10))

        pygame.display.update()
        clock.tick(FPS)
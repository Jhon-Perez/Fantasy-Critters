import pygame
from mod import wn

IMAGE = pygame.image.load("Assets/pikachu.png").convert_alpha()
POKEMON_IMAGE = pygame.transform.scale(IMAGE, (60, 100))

class Critter(pygame.sprite.Sprite):
    def __init__(self, x, y, health, damage, name, score, spriteGroup):
        super().__init__()
        self.image = POKEMON_IMAGE
        self.rect = self.image.get_rect()

        self.health = health
        self.damage = damage
        self.name = name
        self.score = score

        self.rect.x = x
        self.rect.y = y

        spriteGroup.add(self)

    def draw(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))
        

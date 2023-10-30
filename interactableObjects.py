import pygame
from mod import wn

IMAGE = pygame.image.load("Assets/tempGrass.png").convert_alpha()
GRASS_IMAGE = pygame.transform.scale(IMAGE, (60,100))

class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = GRASS_IMAGE
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))

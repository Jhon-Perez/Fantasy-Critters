from mod import *

# IMAGE = pygame.image.load("Assets/pikachu.png").convert_alpha()
# POKEMON_IMAGE = pygame.transform.scale(IMAGE, (60, 100))

# class Critter(pygame.sprite.Sprite):
#     def __init__(self, x, y, health, damage):
#         super().__init__()
#         self.image = POKEMON_IMAGE
#         self.rect = self.image.get_rect()                        Using this for reference for now

#         self.health = health
#         self.damage = damage

#         self.rect.x = x
#         self.rect.y = y

#     def draw(self):
#         wn.blit(self.image, (self.rect.x, self.rect.y))

IMAGE = pygame.image.load("Assets/bush.png").convert_alpha()
GRASS_IMAGE = pygame.transform.scale(IMAGE, (60,100))

class Grass(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=GRASS_IMAGE
        self.rect = self.image.get_rect()
        # spriteGroup.add(self)

        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        IMAGE = pygame.image.load(image_file)

        self.image = IMAGE
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

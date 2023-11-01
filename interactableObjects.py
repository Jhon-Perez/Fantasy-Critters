import pygame
from mod import wn, get_image

GRASS_IMAGE = pygame.image.load("Assets/Sprite_Sheet.png")

class Grass(pygame.sprite.Sprite):
    large_grass = get_image(GRASS_IMAGE, 23, 510, 0, 170, 50)
    small_grass = get_image(GRASS_IMAGE, 197, 510, 0, 95, 50)
    def __init__(self, x, y, grass_size):
        super().__init__()
        if grass_size == "large":
            self.image = self.large_grass
        else:
            self.image = self.small_grass
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))

if __name__ == "__main__":
    import sys
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 60

    large_grass = Grass(20, 20, "large")
    small_grass = Grass(20, 100, "small")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        wn.fill((200, 255, 255))

        large_grass.draw()
        small_grass.draw()

        pygame.display.update()
        clock.tick(FPS)

import sys
from mod import *
from User import User
from critters import Critter
from InteractableObjects import Grass
from InteractableObjects import Background

pygame.init()
pygame.display.set_caption("Test")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
pygame.display.set_caption("Fantasy Critters")

def main():
    user = User(0, 0)
    critter = Critter(300, 100, 100, 5)
    grass = Grass(200,200)

    bg = Background("Assets/Basic BG.png",[0,0])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        wn.fill(WHITE)
        wn.blit(bg.image, bg.rect)

        critter.draw()

        user.movement()
        user.draw()


        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

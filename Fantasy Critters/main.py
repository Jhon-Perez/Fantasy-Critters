import sys
from mod import *
from User import User
from critters import Critter

pygame.init()
pygame.display.set_caption("Test")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)

def main():
    user = User(0, 0)
    critter = Critter(300, 100, 100, 5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        wn.fill(WHITE)

        critter.draw()

        user.movement()
        user.draw()


        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
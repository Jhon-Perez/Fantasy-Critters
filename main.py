import sys
from mod import *
from User import User
from critters import Critter
from InteractableObjects import Grass
from InteractableObjects import Background

pygame.init()

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
pygame.display.set_caption("Fantasy Critters")

def main():
    user = User(0, 0)
    grass = pygame.sprite.Group()  #Maybe add this group to have all the grass things
    grass1 = Grass(200,200)
    grass2 = Grass(260,200)
    grass3 = Grass(200,300)
    grass4 = Grass(260,300)
    critter = Critter(300, 100, 100, 5)

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

        grass1.draw()
        grass2.draw()
        grass3.draw()
        grass4.draw()
        grass.add(grass1,grass2,grass3,grass4) #adding them to the grass group

        if pygame.sprite.spritecollideany(user, grass):
            user.grass(grass1)                 #This is the only issue, you check for if the object user collides with anything in the grass group
                                               #But then the grass function only takes one grass object, I thought about just addding it to the grass object
                                               #But then we would have to check for every grass object, so idk what to do exactly 

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

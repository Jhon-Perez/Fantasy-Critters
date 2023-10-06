import sys, random as rand
from mod import *
from User import User
from critters import Critter
from interactableObjects import Grass
from rooms import Room, check_room

pygame.init()

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
pygame.display.set_caption("Fantasy Critters")

def main():
    user = User(0, 0)

    grass = pygame.sprite.Group()  #Maybe add this group to have all the grass things

    # this still allows you to place grass in specific spots but making an
    # array like this makes it much easier to place and manage
    grass_placement = [
        "xxx",
        "x x",
        "xxx",
    ]
    # gets an array of strings and places grass on all x's
    # very ugly looking function declaration but right now I don't care
    # variable names and formatting are also atrocious but someone can change them
    def place_grass(places, start_x, start_y, increment_x, increment_y):
        for y in range(len(places)):
            for x in range(len(places[y])):
                if places[y][x] == "x":
                    grass.add(Grass(increment_x * x + start_x, increment_y * y + start_y))
    place_grass(grass_placement, 170, 200, 60, 100)

    critters = pygame.sprite.Group()
    critter = Critter(300, 100, 100, 5, critters)

    room1 = Room("Assets/BasicBG.png", (0, 0))
    room2 = Room("Assets/FlippedBG.png", (0, 0))
    current_room = room1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        current_room = check_room(user.rect, current_room, room2)
        wn.blit(current_room.image, current_room.rect)

        critter.draw()

        for g in grass:
            g.draw()
        
        user.movement()
        user.draw()

        # which way of styling do you prefer for if statements?
        # if (pygame.sprite.spritecollideany(user, grass)
        #         and user.moving):
        #         and rand.randint(1, 25) == 1
        #     print("collision")
        #
        # or does this look better?
        if (
            pygame.sprite.spritecollideany(user, grass)
            and user.moving 
            and rand.randint(1, 25) == 1
        ):
            print("collision")

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

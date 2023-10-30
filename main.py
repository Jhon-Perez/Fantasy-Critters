import pygame, sys, random as rand
from mod import wn, WIDTH, HEIGHT
from User import User
from critters import Critter
from interactableObjects import Grass
from rooms import Room, check_room

pygame.init()

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
myfont = pygame.font.SysFont("monospace", 50)
BLACK = (0, 0, 0)
pygame.display.set_caption("Fantasy Critters")

def main():
    user = User(WIDTH/2, HEIGHT/2, 100)

    grass = pygame.sprite.Group()

    critter_var = 0

    critters = pygame.sprite.Group()
    critter1 = Critter(300, 100,  100, 15, "bob", 25, critters)
    critter2 = Critter(350, 150,  100, 25, "alex", 50, critters)
    choice_critter = critter1

    rooms = [
        Room("Assets/BasicBG.png", (0, 0), [
            "   xx    xxxxxx",
            "   xx    xxxxxx",
            "   xx          ",
            "   xx    xxxxxx",
            "   xx    xxxxxx",
            "   xxxxxxxxxxxx"
        ]),
        Room("Assets/FlippedBG.png", (0, 0), [
            "xxxxxx    xx   ",
            "xxxxxx    xx   ",
            "               ",
            "xxxxxx    xx   ",
            "xxxxxx    xx   ",
            "xxxxxxxxxxxx   "
        ])
    ]
    
    fighting_room = Room("Assets/BasicBG.png", (0,0), None)
    before_room = rooms[0]

    current_room = rooms[0]
    check_grass = current_room
    fight_run = ""
    fight_run_font = False
    menu_selection = False
    attack_choice_screen_font = False
    attack_selection = False
    attack_font = False
    attack = 0
    running_font = False

    # gets an array of strings and places grass on all x's
    def place_grass(places, start_x, start_y, increment_x, increment_y):
        for y in range(len(places)):
            for x in range(len(places[y])):
                if places[y][x] == "x":
                    grass.add(Grass(increment_x * x + start_x, increment_y * y + start_y))
    place_grass(rooms[0].grass, 0, 0, 60, 100)

    # BUG: Grass doesn't change when going back to the first room ONLY if a fight with a critter hasn't occured
    def place_room_grass(current_room, check_grass):
        if check_grass == current_room:
            pass
        elif current_room != fighting_room:
            index = rooms.index(current_room)
            grass.empty()
            check_grass = current_room
            # Change into if statements if these parameters need to change
            place_grass(rooms[index].grass, 0, 0, 60, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        current_room = check_room(user.rect, current_room, rooms, fighting_room)
        wn.blit(current_room.image, current_room.rect)
        place_room_grass(current_room, check_grass)

        for g in grass:
            g.draw()

        if current_room == fighting_room:
            if critter_var == 1:
                choice_critter = critter1
                critter1.draw()
            elif critter_var == 2:
                choice_critter=critter2
                critter2.draw()
        else:
            user.movement()
            user.draw()

        # TODO: maybe figure out a way to replace time.delay so that the user has
        # to press a button to continue so they can read at their own pace. There
        # are multiple time.delay throught the program so if you can figure that
        # out here than replace it throught the program.
        if menu_selection:
            fight_run = fighting_room.attack_room_menu_selection()
            if fight_run != None:
                fight_run_font = False
                menu_selection = False
                if fight_run == 'fight':
                    wn.blit(current_room.image, current_room.rect)
                    pygame.time.delay(250)
                    attack_choice_screen_font = True
                else:
                    running_font = True
        
        if running_font:
            fighting_room.running_font()
            pygame.time.delay(1000)
            current_room=before_room
            running_font=False

        if fight_run_font:
            fighting_room.fighting_fight_run_room_fun(fight_run)

        if attack_selection:
            attack = fighting_room.attack_selection()
            if attack != None:
                attack_selection = False
                attack_choice_screen_font = False
                user.attack(choice_critter, attack)
                attack_font = True

        if attack_font:
            fighting_room.attack_font(user, choice_critter, attack)
            attack_font = False
            pygame.time.delay(1500)
            if choice_critter.health > 0:
                attack_selection = True
                attack_choice_screen_font = True
            else:
                choice_critter.health = 100
                current_room = before_room

        if attack_choice_screen_font:
            fighting_room.fighting_game_loop()
            attack_selection = True

        bottom_rect = pygame.Rect(user.rect.left, user.rect.bottom - 10, user.rect.width, 10)
        for sprite in grass:
            if (sprite.rect.colliderect(bottom_rect)
                    and user.moving and rand.randint(1, 10) == 1):
                critter_var = rand.randint(1,2)
                grass.empty()
                before_room, current_room = current_room, fighting_room
                check_grass = current_room
                fight_run_font = True
                menu_selection = True

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

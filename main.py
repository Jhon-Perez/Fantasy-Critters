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
    current_grass = None
    fight_run = ""
    fight_run_font = False
    menu_selection = False
    attack_choice_screen_font = False
    attack_selection = False
    attack_font = False
    attack = 0
    running_font = False
    ask_question = False
    selection = 0

    # gets an array of strings and places grass on all x's
    def place_grass(places, start_x, start_y, increment_x, increment_y):
        for y in range(len(places)):
            for x in range(len(places[y])):
                if places[y][x] == 'x':
                    grass.add(Grass(increment_x * x + start_x, increment_y * y + start_y))
    place_grass(rooms[0].grass, 0, 0, 60, 100)

    def place_room_grass(current_room, current_grass):
        if current_grass == current_room.grass:
            pass
        elif current_room != fighting_room:
            grass.empty()
            current_grass = current_room.grass
            # Change into if statements if these parameters need to change for different rooms
            place_grass(current_grass, 0, 0, 60, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        current_room = check_room(user.rect, current_room, rooms, fighting_room)
        wn.blit(current_room.image, current_room.rect)
        place_room_grass(current_room, current_grass)

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

        # SELECTION:
        # 0 -> Not currently fighting
        # 1 -> Select whether to fight or run
        # 2 -> Display running text / move onto 3
        # 3 -> Ask the user which attack they want to use
        # 4 -> Check whether the critter is dead or not
        # 5 -> Ask a question and do something based of if the user is correct
        if selection == 1:
            fight_run = fighting_room.attack_room_menu_selection()
            fighting_room.fighting_fight_run_room_fun(fight_run)
            if fight_run != None:
                selection = 2
        elif selection == 2:
            if fight_run == "fight":
                selection = 3
                # BUG this is temporary. Right now if I hold 1 it will also immediately choose 1 for the
                # next selection from the previous selection. Right know I don't care about this and it will 
                # stay because I want to focus on making a game that can be presented rather than functional.
                pygame.time.delay(500)
            elif fight_run == "run":
                fighting_room.running_font()
                pygame.time.delay(1000)
                current_room = before_room
                selection = 0
        elif selection == 3:
            fighting_room.fighting_game_loop()
            attack = fighting_room.attack_selection()
            if attack != None:
                selection = 4
        elif selection == 4:
            if choice_critter.health > 0:
                selection = 5
            else:
                choice_critter.health = 100
                current_room = before_room
                selection = 0
        elif selection == 5:
            correct = fighting_room.ask_question()
            if correct:
                user.attack(choice_critter, attack)
                fighting_room.attack_font(user, choice_critter, attack)
                pygame.time.delay(1500)
            else:
                user.attack(choice_critter, 0)
                fighting_room.wrong_attack_font(user, choice_critter)
                pygame.time.delay(1500)
            selection = 3

        bottom_rect = pygame.Rect(user.rect.left, user.rect.bottom - 10, user.rect.width, 10)
        for sprite in grass:
            if (sprite.rect.colliderect(bottom_rect)
                    and user.moving and rand.randint(1, 10) == 1):
                critter_var = rand.randint(1,2)
                grass.empty()
                before_room, current_room = current_room, fighting_room
                current_grass = None
                fight_run_font = True
                menu_selection = True
                selection = 1

        wn.blit(myfont.render(f"Score: {user.score}", 1, BLACK), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

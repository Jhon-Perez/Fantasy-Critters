import pygame, sys, random as rand
from mod import wn, WIDTH, HEIGHT
from User import User
from critters import Critter
from interactableObjects import Grass
from rooms import Room, check_room
from questions import Question

pygame.init()

clock = pygame.time.Clock()
FPS = 60

current_time = 0
animation_cooldown = 250

WHITE = (255, 255, 255)
myfont = pygame.font.SysFont("monospace", 50)
continue_font = pygame.font.SysFont("monospace", 25)
BLACK = (0, 0, 0)
pygame.display.set_caption("Fantasy Critters")

def main():
    user = User(WIDTH/2, HEIGHT/2, 100)

    grass = pygame.sprite.Group()

    critters = [
        Critter(0, 75, 10, "Floofy", 25),
        Critter(1, 85, 15, "Giraldo", 35),
        Critter(2, 110, 40, "Pepe", 80),
        Critter(3, 50, 35, "Venus", 60),
        Critter(4, 125, 20, "Maine", 55),
        Critter(5, 60, 30, "Herbert", 40),
    ]
    choice_critter = None

    rooms = [
        Room("Assets/Background wo leaves.png", (0, 0), [
            "            ",
            "            ",
            "     x      ",
            "   X X X    ",
            "  X X X X   ",
            " X X X X X  ",
            " X X   X X  ",
            "            ",
            "            ",
            " Xx     xX  ",
            "  X     X   ",
            "   X   X    ",
            "    X X     ",
        ]),
        Room("Assets/FlippedBG.png", (0, 0), [])
    ]
    
    fighting_room = Room("Assets/Fighting Screen.png", (0,0), None)
    before_room = rooms[0]

    current_room = rooms[0]
    current_grass = None
    correct = True
    fight_run = ""
    attack = 0
    selection = 0
    continue_information = continue_font.render("Press enter or space to continue", 1, BLACK)
    question = Question()

    # gets an array of strings and places grass on all x's
    def place_grass(places, increment_x, increment_y, start_x = 0, start_y = 0):
        for y in range(len(places)):
            for x in range(len(places[y])):
                if places[y][x] == 'X':
                    grass.add(Grass(increment_x * x + start_x, increment_y * y + start_y, "large"))
                elif places[y][x] == 'x':
                    grass.add(Grass(increment_x * x + start_x, increment_y * y + start_y, "small"))

    def place_room_grass(current_room, current_grass):
        if current_grass == current_room.grass:
            pass
        elif current_room != fighting_room:
            grass.empty()
            current_grass = current_room.grass
            # Change into if statements if these parameters need to change for different rooms
            place_grass(current_grass, 75, 35)

    def press_to_continue():
        wn.blit(continue_information, (350, 0))
        keys_pressed = pygame.key.get_pressed()
        return keys_pressed[pygame.K_RETURN] or keys_pressed[pygame.K_SPACE]

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
            choice_critter.draw()
        else:
            user.movement(current_time, animation_cooldown)
            user.draw()

        # SELECTION:
        # 0 -> Not currently fighting
        # 1 -> Select whether to fight or run
        # 2 -> Display running text / move onto 3
        # 3 -> Ask the user which attack they want to use
        # 4 -> Ask a new question
        # 5 -> Display the new question and wait for input
        # 6 -> Display the attack and health info
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
                if press_to_continue():
                    current_room = before_room
                    selection = 0
        elif selection == 3:
            fighting_room.fighting_game_loop()
            attack = fighting_room.attack_selection()
            if attack != None:
                selection = 4
        elif selection == 4:
            question.new_question()
            pygame.time.delay(1000)
            selection = 5
        elif selection == 5:
            correct = question.display_question()
            if correct != None:
                if correct:
                    user.attack(choice_critter, attack)
                else:
                    user.attack(choice_critter, 0)
                selection = 6
        elif selection == 6:
            if correct:
                fighting_room.attack_font(user, choice_critter, attack)
            else:
                fighting_room.wrong_attack_font(user, choice_critter)
            continued = press_to_continue()
            if choice_critter.health <= 0 and continued:
                choice_critter.health = 100
                selection = 0
                current_room = before_room
                question.clear()
            elif continued:
                selection = 3
                question.clear()

        bottom_rect = pygame.Rect(user.rect.left, user.rect.bottom - 10, user.rect.width, 10)
        for sprite in grass:
            if (sprite.rect.colliderect(bottom_rect)
                    and user.moving and rand.randrange(0, 175) == 69):
                choice_critter = critters[rand.randrange(0, len(critters))]
                grass.empty()
                before_room, current_room = current_room, fighting_room
                current_grass = None
                selection = 1
                break

        wn.blit(continue_font.render(f"Score: {user.score}", 1, BLACK), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

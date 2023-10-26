
import sys, random as rand
import time
from mod import *
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
    user = User(WIDTH/2, HEIGHT/2)

    grass = pygame.sprite.Group()  #Maybe add this group to have all the grass things
    # this still allows you to place grass in specific spots but making an
    # array like this makes it much easier to place and managee
    grass_placement_room1 = [
        "   xx    xxxxxx",
        "   xx    xxxxxx",
        "   xx          ",
        "   xx    xxxxxx",
        "   xx    xxxxxx",
        "   xxxxxxxxxxxx"
    ]
    grass_placement_room2 = [
        "xxxxxx    xx   ",
        "xxxxxx    xx   ",
        "               ",
        "xxxxxx    xx   ",
        "xxxxxx    xx   ",
        "xxxxxxxxxxxx   "
    ]
    # gets an array of strings and places grass on all x's
    # very ugly looking function declaration but right now I don't care
    # variable names and formatting are also atrocious but someone can change them
    def place_grass(places, start_x, start_y, increment_x, increment_y):
        for y in range(len(places)):
            for x in range(len(places[y])):
                if places[y][x] == "x":
                    grass.add(Grass(increment_x * x + start_x, increment_y * y + start_y))
    place_grass(grass_placement_room1, 0, 0, 60, 100)

    def place_room_grass(current_room,check_grass):
        if check_grass ==  current_room:
            pass

        elif current_room==room1:
            grass.empty()
            check_grass=room1
            place_grass(grass_placement_room1, 0, 0, 60, 100)

        elif current_room==room2:
            grass.empty()
            check_grass=room2
            place_grass(grass_placement_room2, 0, 0, 60, 100)

    critter_var=0

    critters = pygame.sprite.Group()
    critter1 = Critter(300, 100,  100, 5, "bob", critters)
    critter2 = Critter(350, 150,  100, 5, "alex", critters)
    choice_critter=critter1

    room1 = Room("Assets/BasicBG.png", (0, 0))
    room2 = Room("Assets/FlippedBG.png", (0, 0))
    fighting_room = Room("Assets/tempFight.png", (0,0))
    before_room=room1

    current_room = room1
    check_grass = current_room
    fight_run=""
    fight_run_font=False
    menu_selection = False
    attack_choice_screen_font = False
    attack_selection = False
    attack_font=False
    attack=0
    running_font=False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        current_room = check_room(user.rect, current_room, room2)
        wn.blit(current_room.image, current_room.rect)
        place_room_grass(current_room, check_grass)

        if critter_var==1:
            choice_critter=critter1
            critter1.draw()
        elif critter_var==2:
            choice_critter=critter2
            critter2.draw()

        for g in grass:
            g.draw()

        if current_room != fighting_room:
            user.movement()
        user.draw()

        if menu_selection:
            fight_run=fighting_room.attack_room_menu_selection()
            if fight_run != None:
                fight_run_font=False
                menu_selection=False
                if fight_run=='fight':
                    wn.blit(current_room.image,current_room.rect)
                    time.sleep(0.25)
                    print('done')
                    attack_choice_screen_font=True
                    print('done2')
                else:
                    running_font=True
                    
        
        if running_font:
            fighting_room.running_font()
            time.sleep(1)
            current_room=before_room
            running_font=False

        if fight_run_font:
            fighting_room.fighting_fight_run_room_fun(fight_run)

        if attack_selection:
            attack=fighting_room.attack_selection()
            if attack != None:
                attack_selection=False
                attack_choice_screen_font=False
                if attack==1:
                    user.attack(choice_critter,1)
                    attack=1
                    attack_font=True
                elif attack==2:
                    user.attack(choice_critter,2)
                    attack=2
                    attack_font=True
                elif attack==3:
                    user.attack(choice_critter,3)
                    attack=3
                    attack_font=True
                elif attack==4:
                    user.attack(choice_critter,4)
                    attack=4
                    attack_font=True

        if attack_font:
            fighting_room.attack_font(choice_critter,attack)
            attack_font=False
            time.sleep(1.5)
            if choice_critter.health>0:
                attack_selection=True
                attack_choice_screen_font=True
            else:
                choice_critter.health=100
                current_room=before_room

        if attack_choice_screen_font:
            fighting_room.fighting_game_loop()
            attack_selection=True

        if (pygame.sprite.spritecollideany(user, grass)
                and user.moving
                and rand.randint(1, 10) == 1):
            critter_var = rand.randint(1,2)
            grass.empty()
            before_room,current_room=current_room,fighting_room
            check_grass=current_room
            fight_run_font=True
            menu_selection=True

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

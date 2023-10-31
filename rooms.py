import pygame, random as rand
from mod import wn, WIDTH, HEIGHT
from questions import question_list

key_mapping = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4
}
BLACK = (0, 0, 0)

class Room(pygame.sprite.Sprite):
    def __init__(self, image_path, location, grass):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.grass = grass

    def attack_room_menu_selection(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_1]:
            return 'fight'
        if keys_pressed[pygame.K_2]:
            return 'run'
        if keys_pressed[pygame.K_3]:
            return 3
        if keys_pressed[pygame.K_4]:
            return 4
    
    # Why are all these fighting room functions in rooms.py? They have no correlation 
    # to rooms. In the future when organizing, making sure the objects are seperated.
    # You can tell these methods don't belong when self is an unused variable. Don't 
    # worry about this it's just a reminder
    def fighting_fight_run_room_fun(self, fight_run):
        myfont = pygame.font.SysFont("monospace", 50)
        run_label = myfont.render(f"2: Run Away", 1, BLACK)
        fight_label = myfont.render(f"1: Fight Critter", 1, BLACK)
        wn.blit(run_label, (100, 500))
        wn.blit(fight_label, (100,450))
        if fight_run == 'fight':
            return 'fight'
        if fight_run == 'run':
            return 'run'
        pygame.display.update()

    def running_font(self):
        myfont = pygame.font.SysFont("monospace", 50)
        run_label = myfont.render(f"Running Away", 1, BLACK)
        wn.blit(run_label, (100,450))
        pygame.display.update()

    # haha funny one liner. You can remove this if you want, I just wanted to be funny.
    def attack_selection(self):
        return next(iter([value for key, value in key_mapping.items() if pygame.key.get_pressed()[key]]), None)
        
    # Try to use lists more, they make code less clunky
    def fighting_game_loop(self):
        myfont = pygame.font.SysFont("monospace", 50)
        attack_labels = [
            myfont.render(f"1: Attack 1, 25 dmg", 1, BLACK),
            myfont.render(f"2: Attack 2, 10 dmg", 1, BLACK),
            myfont.render(f"3: Attack 3, 10 dmg", 1, BLACK),
            myfont.render(f"4: Attack 4, 10 dmg", 1, BLACK)
        ]
        # The reason I reversed the list is so that we can start from the bottom up. Putting the bottom text
        # first so that space doesn't run out if more labels are added to the list. This often times is good
        # practice in programming rather than having to readjust everything just to add one thing This is
        # also the reason why I said it is better to use a list and for-loop style.
        for i, attack_label in enumerate(reversed(attack_labels)):
            wn.blit(attack_label, (10, 500 - 50 * i))
        pygame.display.update()

    def attack_font(self, user, critter, choice):
        myfont = pygame.font.SysFont("monospace", 35)
        if critter.health < 0:
            health = 0
        else:
            health = critter.health
        attack_labels = [
            myfont.render(f"{critter.name} took 25 dmg, {critter.name} is now at {health} health", 1, BLACK),
            myfont.render(f"{critter.name} took 10 dmg, {critter.name} is now at {health} health", 1, BLACK),
            myfont.render(f"{critter.name} took 10 dmg, {critter.name} is now at {health} health", 1, BLACK),
            myfont.render(f"{critter.name} took ∞ dmg, {critter.name} is now at {health} health", 1, BLACK)
        ]
        damage_taken = myfont.render(f"Player took {critter.damage} and is now at {user.health} health", 1, BLACK)
        wn.blit(attack_labels[choice - 1], (10, 425))
        wn.blit(damage_taken, (10, 500))

        if user.health <= 0:
            wn.blit(myfont.render(f"You died :(", 1, BLACK), (WIDTH/2 - 50, HEIGHT/2 - 50))
            pygame.display.update()
            pygame.time.delay(2500)
            pygame.quit()

        pygame.display.update()
    
    def wrong_attack_font(self, user, critter):
        myfont = pygame.font.SysFont("monospace", 35)
        wrong = myfont.render(f"{critter.name} dodged that attack!", 1, BLACK)
        damage_taken = myfont.render(f"Player took {critter.damage} and is now at {user.health} health", 1, BLACK)
        wn.blit(wrong, (10, 425))
        wn.blit(damage_taken, (10, 500))

    # TODO NOW
    # look at the example I have provided in questions.py if anything needs to be changed on my part
    # let me know so I can get at it right away. For now try to work with what is provided and if
    # you can manage to get it working yourself then that would be great, perfect, and awesome.
    def ask_question(self):
        pick = rand.randrange(0, len(question_list))
        passage = question_list[pick]
        question = passage[1]


        # Splits the passage into different lines so that the print looks nice.
        # this might need to change into a list of strings over new line characters
        # when making the text on the actual text
        max_line_length = 50
        current_line = ""
        formatted_question = []


        words = question.split()
        for word in words:
            # Check if adding the word to the current line would exceed the maximum line length
            if len(current_line) + len(word) + 1 <= max_line_length:
                if current_line:
                    current_line += " "
                current_line += word
            # If adding the word would exceed the line length, start a new line    
            else:
                formatted_question.append(current_line)
                current_line = word
        formatted_question.append(current_line)

        answer = passage[7]

        random_choices = passage[3:7]

        # myfont = pygame.font.SysFont("monospace", 50)

        # pasage0 = myfont.render(f"{passage[0]}",1,BLACK)
        # x = [line for line in formatted_question]
        # question1 =myfont.render(f"{' '.join(x)}",1,BLACK)
        # passage2=myfont.render(f"{passage[2]}",1,BLACK)
        # choice1 = myfont.render(f"{1}. {random_choices[0]}",1,BLACK)
        # choice2 = myfont.render(f"{2}. {random_choices[1]}",1,BLACK)
        # choice3 = myfont.render(f"{3}. {random_choices[2]}",1,BLACK)
        # choice4 = myfont.render(f"{4}. {random_choices[3]}",1,BLACK)
        # answer_font = myfont.render(f"{answer}", 1, BLACK)

        print(passage[0])
        for line in formatted_question:
            print(line)
        print()
        print(passage[2])

        print(answer)
        print("answer:", answer)

        choice = int(input("\nAnswer the question correctly for a treat: "))


        if choice == int(answer):
            return True
            #print("yay you are right but I lied about the treat sorry")
        else:
            return False


def run_fight_screen():
    myfont = pygame.font.SysFont("monospace", 50)

def check_room(player, current_room, rooms, fighting_room):
    if current_room == fighting_room:
        return current_room
    index = rooms.index(current_room)
    if player.right > current_room.rect.right and index < len(rooms) - 1:
        player.x = 20
        return rooms[index + 1]
    if player.left < current_room.rect.left + 10 and index > 0:
        player.x = WIDTH - 100
        return rooms[index - 1]
    return current_room

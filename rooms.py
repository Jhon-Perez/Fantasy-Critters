from mod import *

class Room(pygame.sprite.Sprite):
    place_grass = True
    def __init__(self, image_path, location):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        #self.placement = placement
        
    # TODO - Brett figure out how to place different items in     ''
    # different rooms. IDK maybe using parameters, possibly switch statement


    def add_gameplay(self):
        room = 1
        if self.place_grass:
            self.place_grass = True

    # TODO - Brett make a room to brutally beat critters and possibly
    # catch them

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
    
    def fighting_fight_run_room_fun(self,fight_run):
        myfont = pygame.font.SysFont("monospace", 50)
        BLACK = (0, 0, 0)
        run_label = myfont.render(f"2: Run Away", 1, BLACK)
        fight_label = myfont.render(f"1: Fight Critter", 1, BLACK)
        wn.blit(run_label, (100, 500))
        wn.blit(fight_label, (100,450))
        if fight_run=='fight':
            return 'fight'
        if fight_run=='run':
            return 'run'
        pygame.display.update()

    def running_font(self):
        myfont = pygame.font.SysFont("monospace", 50)
        BLACK = (0, 0, 0)
        run_label = myfont.render(f"Running Away", 1, BLACK)
        wn.blit(run_label, (100,450))
        pygame.display.update()


    def attack_selection(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_1]:
            return 1
        if keys_pressed[pygame.K_2]:
            return 2
        if keys_pressed[pygame.K_3]:
            return 3
        if keys_pressed[pygame.K_4]:
            return 4
        
    def fighting_game_loop(self):
        myfont = pygame.font.SysFont("monospace", 50)
        BLACK = (0, 0, 0)
        attack1_label = myfont.render(f"1: Attack 1, 25 dmg", 1, BLACK)
        attack2_label = myfont.render(f"2: Attack 2, 10 dmg", 1, BLACK)
        attack3_label = myfont.render(f"3: Attack 3, 10 dmg", 1, BLACK)
        attack4_label = myfont.render(f"4: Attack 4, 10 dmg", 1, BLACK)
        wn.blit(attack1_label, (10,350))
        wn.blit(attack2_label, (10, 400))
        wn.blit(attack3_label, (10,450))
        wn.blit(attack4_label, (10,500))
        pygame.display.update()

    def attack_font(self,critter,x):
        myfont = pygame.font.SysFont("monospace", 35)
        BLACK = (0, 0, 0)
        if critter.health<0:
            health=0
        else:
            health=critter.health
        if x==1:
            attack1_label = myfont.render(f"{critter.name} took 25 dmg, {critter.name} is now at {health} health", 1, BLACK)
            wn.blit(attack1_label, (10,425))
        if x==2:
            attack1_label = myfont.render(f"{critter.name} took 10 dmg, {critter.name} is now at {health} health", 1, BLACK)
            wn.blit(attack1_label, (10,425))
        if x==3:
            attack1_label = myfont.render(f"{critter.name} took 10 dmg, {critter.name} is now at {health} health", 1, BLACK)
            wn.blit(attack1_label, (10,425))
        if x==4:
            attack1_label = myfont.render(f"{critter.name} took ∞ dmg, {critter.name} is now at {health} health", 1, BLACK)
            wn.blit(attack1_label, (10,425))
        pygame.display.update()



def run_fight_screen():
    myfont = pygame.font.SysFont("monospace", 50)
    BLACK = (0, 0, 0)



# TODO - Jhon figure out how to seperate different transitions
# also right now it only checks x-axis not the ranges for y
def check_room(player, current_room, next_room):
    if player.right > current_room.rect.right:
        player.x = 0
        return next_room
    elif player.left < current_room.rect.left:
        player.x = WIDTH
        return next_room
    elif player.bottom > current_room.rect.bottom:
        player.y = 0
        return next_room
    elif player.top < current_room.rect.top:
        player.y = HEIGHT
        return next_room
    # Add more conditions for other rooms
    return current_room

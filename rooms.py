import pygame, random as rand
from mod import wn, WIDTH, HEIGHT

key_mapping = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4
}
BLACK = (0, 0, 0)
text_box = pygame.image.load("Assets/text_box.png").convert_alpha()
text_box = pygame.transform.scale(text_box, (780, 300))

class Room(pygame.sprite.Sprite):
    def __init__(self, image_path, location, grass):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.grass = grass

    def attack_room_menu_selection(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_1]:
            return 'fight'
        if keys_pressed[pygame.K_2]:
            return 'run'
    
    # Why are all these fighting room functions in rooms.py? They have no correlation 
    # to rooms. In the future when organizing, making sure the objects are seperated.
    # You can tell these methods don't belong when self is an unused variable. Don't 
    # worry about this it's just a tip
    def fighting_fight_run_room_fun(self, fight_run):
        myfont = pygame.font.SysFont("monospace", 50)
        run_label = myfont.render(f"2: Run Away", 1, BLACK)
        fight_label = myfont.render(f"1: Fight Critter", 1, BLACK)
        wn.blit(run_label, (100, 475))
        wn.blit(fight_label, (100, 425))
        if fight_run == 'fight':
            return 'fight'
        if fight_run == 'run':
            return 'run'
        pygame.display.update()

    def running_font(self):
        myfont = pygame.font.SysFont("monospace", 50)
        run_label = myfont.render(f"Running Away", 1, BLACK)
        wn.blit(run_label, (100, 450))
        pygame.display.update()

    # haha funny one liner. You can remove this if you want, I just wanted to be funny.
    def attack_selection(self):
        return next(iter([value for key, value in key_mapping.items() if pygame.key.get_pressed()[key]]), None)
        
    # Try to use lists more, they make code less clunky
    def fighting_game_loop(self):
        myfont = pygame.font.SysFont("monospace", 35)
        attack_labels = [
            myfont.render(f"1: Kick, 25 dmg", 1, BLACK),
            myfont.render(f"2: Punch, 10 dmg", 1, BLACK),
            myfont.render(f"3: Slap, 10 dmg", 1, BLACK),
            myfont.render(f"4: Pet, ∞ dmg", 1, BLACK)
        ]
        wn.blit(attack_labels[0], (50, 430))
        wn.blit(attack_labels[1], (50, 480))
        wn.blit(attack_labels[2], (450, 430))
        wn.blit(attack_labels[3], (450, 480))
        pygame.display.update()

    def attack_font(self, user, critter, choice):
        myfont = pygame.font.SysFont("monospace", 25)
        if critter.health < 0:
            health = 0
        else:
            health = critter.health
        attack_labels = [
            myfont.render(f"{critter.name} took 25 dmg, {critter.name} is now at {health} health", 1, BLACK),
            myfont.render(f"{critter.name} took 10 dmg, {critter.name} is now at {health} health", 1, BLACK),
            myfont.render(f"{critter.name} took 10 dmg, {critter.name} is now at {health} health", 1, BLACK),
            myfont.render(f"{critter.name} took ∞ dmg, {critter.name} is now crippled", 1, BLACK)
        ]
        if critter.health > 0:
            damage_taken = myfont.render(f"Player took {critter.damage} and is now at {user.health} health", 1, BLACK)
        else:
            damage_taken = myfont.render(f"{critter.name} has been knocked out! +{critter.score}", 1, BLACK)
        wn.blit(attack_labels[choice - 1], (50, 425))
        wn.blit(damage_taken, (50, 500))

        if user.health <= 0:
            wn.blit(myfont.render(f"You died :(", 1, BLACK), (WIDTH/2 - 50, HEIGHT/2 - 50))
            pygame.display.update()
            pygame.time.delay(2500)
            pygame.quit()

        pygame.display.update()
    
    def wrong_attack_font(self, user, critter):
        myfont = pygame.font.SysFont("monospace", 25)
        wrong = myfont.render(f"{critter.name} dodged that attack!", 1, BLACK)
        damage_taken = myfont.render(f"Player took {critter.damage} and is now at {user.health} health", 1, BLACK)
        wn.blit(wrong, (50, 425))
        wn.blit(damage_taken, (50, 500))

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

from mod import *

class Room(pygame.sprite.Sprite):
    place_grass = True
    def __init__(self, image_path, location, placement: (int, int)):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.placement = placement
        
    # TODO - Brett figure out how to place different items in
    # different rooms. IDK maybe using parameters, possibly switch statement
    def add_gameplay(self):
        room = 1
        if self.place_grass:
            self.place_grass = True

    # TODO - Brett make a room to brutally beat critters and possibly
    # catch them
    def fighting_room(self):
        pass
        
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

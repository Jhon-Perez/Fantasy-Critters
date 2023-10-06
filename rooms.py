from mod import *

class Room(pygame.sprite.Sprite):
    def __init__(self, image_path, location):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        # Add objects, characters, etc. to the room


# TODO figure out how to seperate different transitions
# also right now it only checks x-axis not the ranges for y
def check_room(player, current_room, next_room):
    if player.right > current_room.rect.right:
        player.x = 0
        return next_room
    # Add more conditions for other rooms
    return current_room

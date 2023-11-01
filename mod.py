import pygame

WIDTH = 900
HEIGHT = 560

wn = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

def get_image(sheet, start_x, start_y, _frame, width, height, scale = 1):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (start_x, start_y, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image
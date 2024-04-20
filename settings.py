import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BROWN = (150,75,0)
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)
font_very_small = pygame.font.SysFont("Verdana", 20)

BG_COLOR = WHITE

FPS = 144

WIDTH, HEIGHT = 1500, 700

CHARACTERISTICS_BAR_WIDTH = 250
CHARACTERISTICS_BAR_HEIGHT = 300

SPEED_OF_CHARACTER = 5

def get_font(size):
    return pygame.font.SysFont("comicsans",size)

#математика всей игры
KBTU_knoweldge_change = 25
KBTU_sleep_change = -20
KBTU_satiety_change = -10
KBTU_happiness_change = -10

dorm_knoweldge_change = -10
dorm_sleep_change = 30
dorm_satiety_change = -10
dorm_happiness_change = -10

cafe_knoweldge_change = -10
cafe_sleep_change = -10
cafe_satiety_change = 25
cafe_happiness_change = -5

SH_knoweldge_change = -15
SH_sleep_change = -5
SH_satiety_change = -5
SH_happiness_change = 20
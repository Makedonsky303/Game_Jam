import pygame, random
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
    return pygame.font.SysFont("comicsansms",size)

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

# Margins
x_margin_for_bars = 30

# Init
gaming = False
course_counter = 1
game_time_sec = -1
game_time_min = 0
flag_buttons = 0
confirmation = None
show_info = False


# Basketball
basketball = False
basketball_timer = 0
bg = pygame.transform.scale(pygame.image.load("basket/bg.png"), (WIDTH, HEIGHT))
bg_rect = bg.get_rect()
ball_radius = 15
gravity = 0.15
drag_strength = 0.03



#loading images
ball_image = pygame.transform.scale(pygame.image.load("basket/ball_image.png"), (30,30))
ring_image = pygame.transform.scale(pygame.image.load("basket/ring_image.png"), (150,150))

ball = pygame.Rect(WIDTH // 2, HEIGHT - 100, 30, 30) #position of the ball
ball_velocity = [0, 0] #initial

ring_x = random.randint(100, HEIGHT - 200) # initial position (random)
ring_y = 150
ring = pygame.Rect(ring_x, ring_y, 100, 10) # ring in the center with width 100 and height 10

#initial states of the game
dragging = False
drag_start_pos = None
score = 0

font = get_font(36)

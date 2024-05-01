import pygame
pygame.init()
from settings import *
from bar import Bar

#спрайты меню
mainScreen = pygame.image.load("screens/mainScreen.png")
mainScreen = pygame.transform.scale(mainScreen,(WIDTH, HEIGHT))
mainScreen_rect = mainScreen.get_rect()

gameScreen = pygame.image.load("screens/mainBackground.png")
gameScreen = pygame.transform.scale(gameScreen,(WIDTH, HEIGHT))
gameScreen_rect = gameScreen.get_rect()

winScreen = pygame.image.load("screens/winScreen.png")
winScreen = pygame.transform.scale(winScreen,(WIDTH, HEIGHT))
winScreen_rect = winScreen.get_rect()

failScreen = pygame.image.load("screens/failScreen.png")
failScreen = pygame.transform.scale(failScreen,(WIDTH, HEIGHT))
failScreen_rect = failScreen.get_rect()

accidentScreen = pygame.image.load("screens/accident_screen.png")
accidentScreen = pygame.transform.scale(accidentScreen,(WIDTH, HEIGHT))
accidentScreen_rect = accidentScreen.get_rect()


background = mainScreen
background_rect = mainScreen_rect

#кнопки игры и само меню
imageBar = pygame.image.load("screens/imageBar.png")
unpbplay = pygame.image.load("buttons/unpbplay.png")
unpbexit = pygame.image.load("buttons/unpbexit.png")
unpbinfo = pygame.image.load("buttons/unpbinfo.png")
pbplay = pygame.image.load("buttons/pbplay.png")
pbexit = pygame.image.load("buttons/pbexit.png")
pbinfo = pygame.image.load("buttons/pbinfo.png")

unpb_yes = pygame.image.load("buttons/unpb-yes.png")
unpb_no = pygame.image.load("buttons/unpb-no.png")
pb_yes = pygame.image.load("buttons/pb-yes.png")
pb_no = pygame.image.load("buttons/pb-no.png")

#коррекция масштаба кнопок и их rectangles
imageBar = pygame.transform.scale(imageBar,(CHARACTERISTICS_BAR_WIDTH, CHARACTERISTICS_BAR_HEIGHT + 20))
imageBar_rect = imageBar.get_rect()

info = pygame.image.load("screens/info.png") 
info_rect = info.get_rect(center = (WIDTH//2 + 25, HEIGHT//2))

condition = pygame.transform.scale(imageBar,(350, 200))
condition_rect = condition.get_rect(center = (WIDTH//2 + 75, HEIGHT//2 - 100))

unpbplay_small = pygame.transform.scale(unpbplay,(350,150))
unpbplay_small_rect = unpbplay_small.get_rect()
unpbplay_small_rect.center = (775,325)
unpbexit_small = pygame.transform.scale(unpbexit,(350,150))
unpbexit_small_rect = unpbexit_small.get_rect()
unpbexit_small_rect.center = (775,475)
unpbinfo_small = pygame.transform.scale(unpbinfo,(350,150))
unpbinfo_small_rect = unpbinfo_small.get_rect()
unpbinfo_small_rect.center = (775,625)
pbplay_small = pygame.transform.scale(pbplay,(350,150))
pbplay_small_rect = pbplay_small.get_rect()
pbplay_small_rect.center = (775,325)
pbexit_small = pygame.transform.scale(pbexit,(350,150))
pbexit_small_rect = pbexit_small.get_rect()
pbexit_small_rect.center = (775,475)
pbinfo_small = pygame.transform.scale(pbinfo,(350,150))
pbinfo_small_rect = pbinfo_small.get_rect()
pbinfo_small_rect.center = (775,625)

unpb_yes_small = pygame.transform.scale(unpb_yes,(100, 50))
unpb_yes_small_rect = unpb_yes_small.get_rect(center = (700, 400))
unpb_no_small = pygame.transform.scale(unpb_no,(105, 55))
unpb_no_small_rect = unpb_no_small.get_rect(center = (950, 400))
pb_yes_small = pygame.transform.scale(pb_yes,(100, 50))
pb_yes_small_rect = pb_yes_small.get_rect(center = (700, 400))
pb_no_small = pygame.transform.scale(pb_no,(105, 55))
pb_no_small_rect = pb_no_small.get_rect(center = (950, 400))

#спрайты зданий снаружи
kbtu_outside = pygame.image.load("buildings_outside/kbtuu.png")
kbtu_outside_small = pygame.transform.scale(kbtu_outside, (350, 200))
kbtu_outside_small_rect = kbtu_outside_small.get_rect()
kbtu_outside_small_rect.center = (625, 170)
dormitory_outside = pygame.image.load("buildings_outside/dormOutside.png")
dormitory_outside_small = pygame.transform.scale(dormitory_outside, (350, 200))
dormitory_outside_small_rect = dormitory_outside_small.get_rect()
dormitory_outside_small_rect.center = (1175, 170)
cinema_outside = pygame.image.load("buildings_outside/cinema.png")
cinema_outside_small = pygame.transform.scale(cinema_outside, (350, 200))
cinema_outside_small_rect = cinema_outside_small.get_rect()
cinema_outside_small_rect.center = (625, 550)
cafe_outside = pygame.image.load("buildings_outside/cafeOutside.png")
cafe_outside_small = pygame.transform.scale(cafe_outside, (351, 200))
cafe_outside_small_rect = cafe_outside_small.get_rect()
cafe_outside_small_rect.center = (1176, 555)
 
#внутренности зданий
kbtu_inside = pygame.image.load("buildings_inside/kbtu-inside.png")
kbtu_inside = pygame.transform.scale(kbtu_inside, (WIDTH, HEIGHT))
kbtu_inside_rect = kbtu_inside.get_rect()
kbtu_inside_rect.center = (WIDTH//2, HEIGHT//2)
dormitory_inside = pygame.image.load("buildings_inside/dormitory.png")
dormitory_inside = pygame.transform.scale(dormitory_inside, (WIDTH, HEIGHT))
dormitory_inside_rect = dormitory_inside.get_rect()
dormitory_inside_rect.center = (WIDTH//2, HEIGHT//2)
cinema_inside = pygame.image.load("buildings_inside/film.png")
cinema_inside = pygame.transform.scale(cinema_inside, (WIDTH + 150, HEIGHT + 160))
cinema_inside_rect = cinema_inside.get_rect()
cinema_inside_rect.center = (WIDTH//2, HEIGHT//2 + 35)
cafe_inside = pygame.image.load("buildings_inside/cafe-inside.png")
cafe_inside = pygame.transform.scale(cafe_inside, (WIDTH, HEIGHT))
cafe_inside_rect = cafe_inside.get_rect()
cafe_inside_rect.center = (WIDTH//2, HEIGHT//2)

#спрайты характеристик студента
knowledge = pygame.image.load("stat sprites/knowledge.png")
knowledge = pygame.transform.scale(knowledge, (40, 40))
knowledge_position_rect = knowledge.get_rect()
knowledge_position_rect.center = (30, 40)
sleep = pygame.image.load("stat sprites/sleep.png")
sleep = pygame.transform.scale(sleep, (120, 120))
sleep_position_rect = sleep.get_rect()
sleep_position_rect.center = (52, 93)
satiety = pygame.image.load("stat sprites/satiety.png")
satiety = pygame.transform.scale(satiety, (70, 70))
satiety_position_rect = satiety.get_rect()
satiety_position_rect.center = (34, 110)
happiness = pygame.image.load("stat sprites/smile.png")
happiness_position_rect = happiness.get_rect()
happiness_position_rect.center = (33, 148)



#звуки кнопок и зданий
pygame.mixer.music.load("zvuk/A_Bit_Of_Hope_-_David_Fesliyan.mp3")
pobeda = pygame.mixer.Sound("zvuk/den-pobedy.mp3")
unluck = pygame.mixer.Sound("zvuk/unluck.mp3")
knopka = pygame.mixer.Sound("zvuk/zvuk-knopki.mp3")
cinema_sound = pygame.mixer.Sound("zvuk/ahhhh-sound.mp3")
kbtu_sound = pygame.mixer.Sound("zvuk/bell.mp3")
dormitory_sound = pygame.mixer.Sound("zvuk/hrap.mp3")
cafe_sound = pygame.mixer.Sound("zvuk/cash_register.mp3")
crash_sound = pygame.mixer.Sound("zvuk/crash.mp3")



# Шкалы характеристик

knowledge_bar = Bar(x_margin_for_bars,30,200,25,100,BROWN)
knowledge_bar.unit = 0
sleep_bar = Bar(x_margin_for_bars,65,200,25,100,BLUE)
satiety_bar = Bar(x_margin_for_bars,100,200,25,100,RED)
happiness_bar = Bar(x_margin_for_bars,135,200,25,100,YELLOW)
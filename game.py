import pygame, sys, time
from settings import *
from bar import Bar
from game_functions import draw_all_game
from Student_ import Student
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

S1 = Student()

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

# Шкалы характеристик
x_margin_for_bars = 30
knowledge_bar = Bar(x_margin_for_bars,30,200,25,100,BROWN)
knowledge_bar.unit = 0
sleep_bar = Bar(x_margin_for_bars,65,200,25,100,BLUE)
satiety_bar = Bar(x_margin_for_bars,100,200,25,100,RED)
happiness_bar = Bar(x_margin_for_bars,135,200,25,100,YELLOW)


#звуки кнопок и зданий
pygame.mixer.music.load("zvuk/A_Bit_Of_Hope_-_David_Fesliyan.mp3")
pobeda = pygame.mixer.Sound("zvuk/den-pobedy.mp3")
unluck = pygame.mixer.Sound("zvuk/unluck.mp3")
knopka = pygame.mixer.Sound("zvuk/zvuk-knopki.mp3")
cinema_sound = pygame.mixer.Sound("zvuk/ahhhh-sound.mp3")
kbtu_sound = pygame.mixer.Sound("zvuk/bell.mp3")
dormitory_sound = pygame.mixer.Sound("zvuk/hrap.mp3")
cafe_sound = pygame.mixer.Sound("zvuk/cash_register.mp3")


#Ingame timer
game_time_sec = -1
game_time_min = 0
game_time_fonts = pygame.font.SysFont('comicsansms', 30)
game_time_text = game_time_fonts.render(f"Time: {game_time_min}:{game_time_sec}", True, (0, 0, 0))
game_time_rect = game_time_text.get_rect()
game_time_rect.center = (120 , 250)

#Time counter
TIME_COUNT_SEC = pygame.USEREVENT + 2
pygame.time.set_timer(TIME_COUNT_SEC, 1000)

# Определяем кнопки заранее
#yes_button = pygame.Rect(650, 350, 100, 50)
#no_button = pygame.Rect(900, 350, 100, 50)

collected_points_text = font_very_small.render("If you enter you will get:", True, (0, 0, 0))
collected_points_text_rect = collected_points_text.get_rect(center=(WIDTH//2 + 75, HEIGHT//2 - 150))


def ask_confirmation(screen, confirmation_text, confirmation_text_rect, know, slee, sati, happ):
            
    know_text = font_very_small.render(f"Knowledge {know}", True, (0, 0, 0))
    know_text_rect = know_text.get_rect(center=(WIDTH//2 + 75, HEIGHT//2 - 125))
    slee_text = font_very_small.render(f"Sleep {slee}", True, (0, 0, 0))
    slee_text_rect = slee_text.get_rect(center=(WIDTH//2 + 75, HEIGHT//2 - 100))
    sati_text = font_very_small.render(f"Satiety {sati}", True, (0, 0, 0))
    sati_text_rect = sati_text.get_rect(center=(WIDTH//2 + 75, HEIGHT//2 - 75))
    happ_text = font_very_small.render(f"Happiness {happ}", True, (0, 0, 0))
    happ_text_rect = happ_text.get_rect(center=(WIDTH//2 + 75, HEIGHT//2 - 50))

    screen.blit(unpb_yes_small, unpb_yes_small_rect)
    screen.blit(unpb_no_small, unpb_no_small_rect)
    screen.blit(condition, condition_rect)

    screen.blit(confirmation_text, confirmation_text_rect)
    screen.blit(collected_points_text, collected_points_text_rect)
    screen.blit(know_text, know_text_rect)
    screen.blit(slee_text, slee_text_rect)
    screen.blit(sati_text, sati_text_rect)
    screen.blit(happ_text, happ_text_rect)

    pygame.display.flip()

gaming = False
course_counter = 1
flag_buttons = 0
confirmation = None
show_info = False

background = mainScreen
background2 = mainScreen_rect
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
while True:
    clock.tick(FPS)
    pressed = pygame.key.get_pressed()
    screen.blit(background, background2)

    for event in pygame.event.get():
        #условия для выхода из игры
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        #условия для кнопок подтверждения
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if unpbplay_small_rect.collidepoint(mouse_pos) and flag_buttons == 0:
                screen.blit(pbplay_small,pbplay_small_rect)
                screen.blit(unpbexit_small, unpbexit_small_rect)
                screen.blit(unpbinfo_small, unpbinfo_small_rect)
                pygame.display.flip()
                background = gameScreen
                background2 = gameScreen_rect

            elif unpbexit_small_rect.collidepoint(mouse_pos) and flag_buttons == 0:
                screen.blit(unpbplay_small,unpbplay_small_rect)
                screen.blit(pbexit_small, pbexit_small_rect)
                screen.blit(unpbinfo_small, unpbinfo_small_rect)
                pygame.display.update()
            elif unpbinfo_small_rect.collidepoint(mouse_pos) and flag_buttons == 0:
                screen.blit(unpbplay_small,unpbplay_small_rect)
                screen.blit(unpbexit_small, unpbexit_small_rect)
                screen.blit(pbinfo_small, pbinfo_small_rect)
                pygame.display.update()

            elif unpb_yes_small_rect.collidepoint(mouse_pos):
                screen.blit(pb_yes_small, pb_yes_small_rect)
                confirmation = True
                draw_all_game(screen, imageBar, imageBar_rect,kbtu_outside_small,kbtu_outside_small_rect,dormitory_outside_small,dormitory_outside_small_rect
                  ,cinema_outside_small,cinema_outside_small_rect,cafe_outside_small,cafe_outside_small_rect, pb_yes_small,pb_yes_small_rect,
                  knowledge,knowledge_position_rect,sleep,sleep_position_rect,satiety,satiety_position_rect,happiness,happiness_position_rect, knowledge_points, knowledge_points_rect, 
                  sleep_points, sleep_points_rect, satiety_points, satiety_points_rect, happiness_points, happiness_points_rect, course_counter_text, course_counter_text_rect, game_time_text, game_time_rect, 
                  knowledge_bar,  sleep_bar, satiety_bar, happiness_bar,
                  unpb_no_small, unpb_no_small_rect, unpb_no_small, unpb_no_small_rect)
                pygame.display.update()
                #pygame.display.flip() #если закоментить pygame.display.flip() то анимации нет и она не дерганая
            elif unpb_no_small_rect.collidepoint(mouse_pos):
                screen.blit(pb_no_small, pb_no_small_rect)
                confirmation = False
                draw_all_game(screen, imageBar, imageBar_rect,kbtu_outside_small,kbtu_outside_small_rect,dormitory_outside_small,dormitory_outside_small_rect
                  ,cinema_outside_small,cinema_outside_small_rect,cafe_outside_small,cafe_outside_small_rect, pb_no_small,pb_no_small_rect,
                  knowledge,knowledge_position_rect,sleep,sleep_position_rect,satiety,satiety_position_rect,happiness,happiness_position_rect, knowledge_points, knowledge_points_rect, 
                  sleep_points, sleep_points_rect, satiety_points, satiety_points_rect, happiness_points, happiness_points_rect, course_counter_text, course_counter_text_rect, game_time_text, game_time_rect, 
                  knowledge_bar,  sleep_bar, satiety_bar, happiness_bar,
                  unpb_yes_small, unpb_yes_small_rect, unpb_yes_small, unpb_yes_small_rect)
                pygame.display.update()
                #pygame.display.flip() #если закоментить pygame.display.flip() то анимации нет и она не дерганая
##################################################################################################################################################

            
        #условия для счетчика времени
        if event.type == TIME_COUNT_SEC and gaming == True:
                game_time_sec += 1
                if game_time_sec == 60 and gaming == True:
                    game_time_min += 1
                    game_time_sec = 0

        #условия проигрыша
        if sleep_bar.unit <= 0 or satiety_bar.unit <= 0 or happiness_bar.unit <= 0:
            screen.blit(failScreen, failScreen_rect)
            pygame.mixer.music.pause()
            unluck.play()
            pygame.display.flip()
            time.sleep(5)
            pygame.quit()
            sys.exit()
    
        #добавляю выбор кнопок мышкой (для info пока не добавлял)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                if unpbplay_small_rect.collidepoint(mouse_pos) and flag_buttons == 0:  
                    knopka.play()
                    time.sleep(1)
                    gaming = True
                    flag_buttons = 1
                elif unpbexit_small_rect.collidepoint(mouse_pos) and flag_buttons == 0:
                    knopka.play()
                    time.sleep(0.5)
                    pygame.quit()
                    sys.exit()
                elif unpbinfo_small_rect.collidepoint(mouse_pos) and flag_buttons == 0:
                    knopka.play()
                    if show_info == False:
                        show_info = True
                    else:
                        show_info = False
                    time.sleep(0.5)
                elif unpb_yes_small_rect.collidepoint(mouse_pos):
                    screen.blit(pb_yes_small, pb_yes_small_rect)
                    knopka.play()
                    time.sleep(0.3) 
                elif unpb_no_small_rect.collidepoint(mouse_pos):
                    screen.blit(pb_no_small, pb_no_small_rect)
                    knopka.play()
                    time.sleep(0.3) 
        
    if gaming:
        screen.blit(imageBar, imageBar_rect)

        #на память коменты оставил (:
        #после добавки спрайтов зданий эти прямоугольники нужно убрать
        pygame.draw.rect(screen, WHITE, (CHARACTERISTICS_BAR_WIDTH+200,70, 350, 200))
        pygame.draw.rect(screen, (152, 136, 131), (CHARACTERISTICS_BAR_WIDTH+200,170, 350, 100))
        pygame.draw.rect(screen, (152, 136, 131), (CHARACTERISTICS_BAR_WIDTH+200,455, 350, 100))
        
        #здания
        screen.blit(kbtu_outside_small, kbtu_outside_small_rect)
        screen.blit(dormitory_outside_small, dormitory_outside_small_rect)
        screen.blit(cinema_outside_small, cinema_outside_small_rect)
        screen.blit(cafe_outside_small, cafe_outside_small_rect)

        S1.move()
        S1.draw(screen)

        #числовые показатели статистики
        knowledge_points = font_small.render(f"{knowledge_bar.unit}", True, (0, 0, 0))
        knowledge_points_rect = knowledge_points.get_rect(center = (120, 40))
        sleep_points = font_small.render(f"{sleep_bar.unit}", True, (0, 0, 0))
        sleep_points_rect = sleep_points.get_rect(center = (120, 75))
        satiety_points = font_small.render(f"{satiety_bar.unit}", True, (0, 0, 0))
        satiety_points_rect = satiety_points.get_rect(center = (120, 110))
        happiness_points = font_small.render(f"{happiness_bar.unit}", True, (0, 0, 0))
        happiness_points_rect = happiness_points.get_rect(center = (120, 145))

        #статистика
        knowledge_bar.draw(screen)
        screen.blit(knowledge_points, knowledge_points_rect)

        sleep_bar.draw(screen)
        screen.blit(sleep_points, sleep_points_rect)

        satiety_bar.draw(screen)
        screen.blit(satiety_points, satiety_points_rect)

        happiness_bar.draw(screen)
        screen.blit(happiness_points, happiness_points_rect)

        screen.blit(knowledge, knowledge_position_rect)
        screen.blit(sleep, sleep_position_rect)
        screen.blit(satiety, satiety_position_rect)
        screen.blit(happiness, happiness_position_rect)
        
        #курс
        course_counter_text = font_small.render(f'Year: {course_counter}', True, (255, 255, 255))
        course_counter_text_rect = course_counter_text.get_rect()
        course_counter_text_rect.center = (120, 200)
        screen.blit(course_counter_text, course_counter_text_rect)

        #Game timer
        game_time_text = game_time_fonts.render(f"Time: {game_time_min}:{game_time_sec}", True, (255, 255, 255))
        screen.blit(game_time_text, game_time_rect)


        if S1.rect.colliderect(dormitory_outside_small_rect):
            confirmation_text = font_small.render("BUILDING: Dormitory", True, (0, 0, 0))
            confirmation_text_rect = confirmation_text.get_rect(center=(WIDTH//2 + 75, HEIGHT//2 - 175))
            ask_confirmation(screen, confirmation_text, confirmation_text_rect, dorm_knoweldge_change, dorm_sleep_change, dorm_satiety_change, dorm_happiness_change)
            # Проверяем подтверждение после выхода из функции

            if confirmation:
                if sleep_bar.unit + dorm_sleep_change < 100:
                    sleep_bar.unit += dorm_sleep_change
                    if knowledge_bar.unit >= dorm_knoweldge_change:
                        knowledge_bar.unit += dorm_knoweldge_change
                    if knowledge_bar.unit <= 0:
                        knowledge_bar.unit = 0
                    if satiety_bar.unit >= dorm_satiety_change:
                        satiety_bar.unit += dorm_satiety_change
                    if happiness_bar.unit >= dorm_happiness_change:
                        happiness_bar.unit += dorm_happiness_change
                else:
                    sleep_bar.unit = 100
                    if knowledge_bar.unit >= dorm_knoweldge_change:
                        knowledge_bar.unit += dorm_knoweldge_change
                    if knowledge_bar.unit <= 0:
                        knowledge_bar.unit = 0
                    if satiety_bar.unit >= dorm_satiety_change:
                        satiety_bar.unit += dorm_satiety_change
                    if happiness_bar.unit >= dorm_happiness_change:
                        happiness_bar.unit += dorm_happiness_change
                
                screen.blit(dormitory_inside, dormitory_inside_rect)
                dormitory_sound.play()
                pygame.mixer.music.pause()
                pygame.display.flip()
                S1.rect.center = (1175, HEIGHT//2)
                time.sleep(2)
                game_time_sec -= 2
                confirmation = None
            elif confirmation == False:
                confirmation = None
                S1.rect.center = (1175, HEIGHT//2)
                pass
            pygame.mixer.music.unpause()


        if S1.rect.colliderect(cinema_outside_small_rect):
            confirmation_text = font_small.render("BUILDING: Cinema", True, (0, 0, 0))
            confirmation_text_rect = confirmation_text.get_rect(center=(WIDTH//2 + 75, HEIGHT//2 - 175))
            ask_confirmation(screen, confirmation_text, confirmation_text_rect, SH_knoweldge_change, SH_sleep_change, SH_satiety_change, SH_happiness_change)
            # Проверяем подтверждение после выхода из функции

            if confirmation:
                if happiness_bar.unit + SH_happiness_change <= 100:
                    happiness_bar.unit += SH_happiness_change
                    if knowledge_bar.unit >= SH_knoweldge_change:
                        knowledge_bar.unit += SH_knoweldge_change
                    if knowledge_bar.unit <= 0:
                        knowledge_bar.unit = 0
                    if satiety_bar.unit >= SH_satiety_change:
                        satiety_bar.unit += SH_satiety_change
                    if sleep_bar.unit >= SH_sleep_change:
                        sleep_bar.unit += SH_sleep_change
                else:
                    happiness_bar.unit = 100
                    if knowledge_bar.unit >= SH_knoweldge_change:
                        knowledge_bar.unit += SH_knoweldge_change
                    if knowledge_bar.unit <= 0:
                        knowledge_bar.unit = 0
                    if satiety_bar.unit >= SH_satiety_change:
                        satiety_bar.unit += SH_satiety_change
                    if sleep_bar.unit >= SH_sleep_change:
                        sleep_bar.unit += SH_sleep_change
                
                screen.blit(cinema_inside, cinema_inside_rect)
                cinema_sound.play()
                pygame.mixer.music.pause()
                pygame.display.flip()
                S1.rect.center = (625, HEIGHT//2)
                time.sleep(2)
                game_time_sec -= 2
                confirmation = None
            elif confirmation == False:
                confirmation = None
                S1.rect.center = (625, HEIGHT//2)
                pass
            pygame.mixer.music.unpause()


        if S1.rect.colliderect(cafe_outside_small_rect):
                confirmation_text = font_small.render("BUILDING: Cafe", True, (0, 0, 0))
                confirmation_text_rect = confirmation_text.get_rect(center=(WIDTH//2 + 75, HEIGHT//2 - 175))
                ask_confirmation(screen, confirmation_text, confirmation_text_rect, cafe_knoweldge_change, cafe_sleep_change, cafe_satiety_change, cafe_happiness_change)
                # Проверяем подтверждение после выхода из функции

                if confirmation:
                    if satiety_bar.unit + cafe_satiety_change <= 100:
                        satiety_bar.unit += cafe_satiety_change
                        if knowledge_bar.unit >= cafe_knoweldge_change:
                            knowledge_bar.unit += cafe_knoweldge_change
                        if knowledge_bar.unit <= 0:
                            knowledge_bar.unit = 0
                        if happiness_bar.unit >= cafe_happiness_change:
                            happiness_bar.unit += cafe_happiness_change
                        if sleep_bar.unit >= cafe_sleep_change:
                            sleep_bar.unit += cafe_sleep_change
                    else:
                        satiety_bar.unit = 100
                        if knowledge_bar.unit >= cafe_knoweldge_change:
                            knowledge_bar.unit += cafe_knoweldge_change
                        if knowledge_bar.unit <= 0:
                            knowledge_bar.unit = 0
                        if happiness_bar.unit >= cafe_happiness_change:
                            happiness_bar.unit += cafe_happiness_change
                        if sleep_bar.unit >= cafe_sleep_change:
                            sleep_bar.unit += cafe_sleep_change
                    
                    screen.blit(cafe_inside, cafe_inside_rect)
                    cafe_sound.play()
                    pygame.mixer.music.pause()
                    pygame.display.flip()
                    S1.rect.center = (1175, HEIGHT//2)
                    time.sleep(2)
                    game_time_sec -= 2
                    confirmation = None
                elif confirmation == False:
                    confirmation = None
                    S1.rect.center = (1175, HEIGHT//2)
                    pass
                pygame.mixer.music.unpause()


        if S1.rect.colliderect(kbtu_outside_small_rect):
            confirmation_text = font_small.render("BUILDING: KBTU", True, (0, 0, 0))
            confirmation_text_rect = confirmation_text.get_rect(center=(WIDTH//2 + 50, HEIGHT//2 - 175))
            ask_confirmation(screen, confirmation_text, confirmation_text_rect, KBTU_knoweldge_change, KBTU_sleep_change, KBTU_satiety_change, KBTU_happiness_change)
            # Проверяем подтверждение после выхода из функции

            if confirmation:
                if knowledge_bar.unit<100:
                    if knowledge_bar.unit+KBTU_knoweldge_change>=100:
                        knowledge_bar.unit += KBTU_knoweldge_change
                        course_counter += 1
                        knowledge_bar.unit -= 100
                        sleep_bar.unit += 20
                        satiety_bar.unit += 20
                        happiness_bar.unit += 20
                        if course_counter >= 5:
                            screen.blit(winScreen, winScreen_rect)
                            game_win_time = font_small.render(f"Your Time : {game_time_min}:{game_time_sec}", True, (0, 0, 0))
                            screen.blit(game_win_time, (WIDTH-300, HEIGHT-100))
                            pygame.mixer.music.pause()
                            pobeda.play()
                            pygame.display.flip()
                            time.sleep(5)
                            pygame.quit()
                            sys.exit()
                    else:
                        knowledge_bar.unit += KBTU_knoweldge_change
                    if sleep_bar.unit>=KBTU_sleep_change:
                        sleep_bar.unit += KBTU_sleep_change
                    if satiety_bar.unit>=KBTU_satiety_change:
                        satiety_bar.unit += KBTU_satiety_change
                    if happiness_bar.unit>=KBTU_happiness_change:
                        happiness_bar.unit += KBTU_happiness_change 
                screen.blit(kbtu_inside, kbtu_inside_rect)
                kbtu_sound.play()
                pygame.mixer.music.pause()
                pygame.display.flip()
                S1.rect.center = (625, HEIGHT//2)
                time.sleep(2)
                game_time_sec -= 2
                confirmation = None
            elif confirmation == False:
                confirmation = None
                S1.rect.center = (625, HEIGHT//2)
                pass
            pygame.mixer.music.unpause()

        if S1.rect.left >= 280 and S1.rect.right <= 390 and S1.rect.top <= 6:
            S1.rect.center = (95, HEIGHT - 35)
        if S1.rect.left <= 6 and S1.rect.bottom <= 430 and S1.rect.top >= 320:
            S1.rect.center = (WIDTH - 35, 360)
        if S1.rect.left >= 40 and S1.rect.right <= 150 and S1.rect.bottom >= HEIGHT - 6:
            S1.rect.center = (335, 35)
        if S1.rect.right >= WIDTH - 6 and S1.rect.bottom <= 430 and S1.rect.top >= 320:
            S1.rect.center = (35, 360)


    elif show_info == 1:
        screen.blit(info, info_rect)
        screen.blit(unpbinfo_small, unpbinfo_small_rect)
        pygame.display.update()
    else:
        screen.blit(unpbplay_small,unpbplay_small_rect)
        screen.blit(unpbexit_small, unpbexit_small_rect)
        screen.blit(unpbinfo_small, unpbinfo_small_rect)   

    pygame.display.flip() 
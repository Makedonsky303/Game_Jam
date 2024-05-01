import pygame, sys, time
from settings import *
from sprites import *
from game_functions import draw_all_game, ask_confirmation
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

#Time counter
TIME_COUNT_SEC = pygame.USEREVENT + 2
pygame.time.set_timer(TIME_COUNT_SEC, 1000)

pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

while True:
    clock.tick(FPS)
    pressed = pygame.key.get_pressed()

    screen.blit(background, background_rect)

    for event in pygame.event.get():
        #условия для выхода из игры
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        #условия для счетчика времени
        if event.type == TIME_COUNT_SEC and gaming == True:
                game_time_sec += 1
                if game_time_sec == 60 and gaming == True:
                    game_time_min += 1
                    game_time_sec = 0

        #условия для кнопок подтверждения
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if unpbplay_small_rect.collidepoint(mouse_pos) and flag_buttons == 0:
                screen.blit(pbplay_small,pbplay_small_rect)
                screen.blit(unpbexit_small, unpbexit_small_rect)
                screen.blit(unpbinfo_small, unpbinfo_small_rect)
                pygame.display.flip()
                background = gameScreen
                background_rect = gameScreen_rect

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
                S1.draw(screen)
                for auto in autos:
                    auto.draw(screen)

                pygame.display.update()

            elif unpb_no_small_rect.collidepoint(mouse_pos):
                screen.blit(pb_no_small, pb_no_small_rect)
                confirmation = False
                draw_all_game(screen, imageBar, imageBar_rect,kbtu_outside_small,kbtu_outside_small_rect,dormitory_outside_small,dormitory_outside_small_rect
                  ,cinema_outside_small,cinema_outside_small_rect,cafe_outside_small,cafe_outside_small_rect, pb_no_small,pb_no_small_rect,
                  knowledge,knowledge_position_rect,sleep,sleep_position_rect,satiety,satiety_position_rect,happiness,happiness_position_rect, knowledge_points, knowledge_points_rect, 
                  sleep_points, sleep_points_rect, satiety_points, satiety_points_rect, happiness_points, happiness_points_rect, course_counter_text, course_counter_text_rect, game_time_text, game_time_rect, 
                  knowledge_bar,  sleep_bar, satiety_bar, happiness_bar,
                  unpb_yes_small, unpb_yes_small_rect, unpb_yes_small, unpb_yes_small_rect)
                S1.draw(screen)
                for auto in autos:
                    auto.draw(screen)
                pygame.display.update()
                


        #условия проигрыша
        if sleep_bar.unit <= 0 or satiety_bar.unit <= 0 or happiness_bar.unit <= 0:
            screen.blit(failScreen, failScreen_rect)
            pygame.mixer.music.pause()
            unluck.play()
            pygame.display.flip()
            time.sleep(5)

            sleep_bar.unit = 100 
            satiety_bar.unit = 100
            happiness_bar.unit = 100
            knowledge_bar.unit = 0 
            course_counter = 1
            game_time_sec = 0
            game_time_min = 0
            gaming = False
            background = mainScreen
            background_rect = mainScreen_rect
            flag_buttons = 0
            S1 = Student()
            A1.restart()
            A2.restart()
            pygame.display.flip()
            pygame.mixer.music.unpause()
    
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

        for auto in autos:
            auto.move()
            auto.draw(screen)

        if pygame.sprite.spritecollideany(S1, autos):
            screen.blit(accidentScreen, accidentScreen_rect)
            pygame.mixer.music.pause()
            crash_sound.play()
            pygame.display.flip()
            time.sleep(5)

            sleep_bar.unit = 100 
            satiety_bar.unit = 100
            happiness_bar.unit = 100
            knowledge_bar.unit = 0 
            course_counter = 1
            game_time_sec = 0
            game_time_min = 0
            gaming = False
            background = mainScreen
            background_rect = mainScreen_rect
            flag_buttons = 0
            S1 = Student()
            A1.restart()
            A2.restart()
            pygame.display.flip()
            pygame.mixer.music.unpause()

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
                S1.rect.center = (WIDTH//2+150, HEIGHT//2-100)
                time.sleep(2)
                game_time_sec -= 2
                confirmation = None
            elif confirmation == False:
                confirmation = None
                S1.rect.center = (WIDTH//2+150, HEIGHT//2-100)
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
                S1.rect.center = (WIDTH//2+150, HEIGHT//2+150)
                time.sleep(2)
                game_time_sec -= 2
                confirmation = None
            elif confirmation == False:
                confirmation = None
                S1.rect.center = (WIDTH//2+150, HEIGHT//2+150)
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
                    S1.rect.center = (WIDTH//2+150, HEIGHT//2+150)
                    time.sleep(2)
                    game_time_sec -= 2
                    confirmation = None
                elif confirmation == False:
                    confirmation = None
                    S1.rect.center = (WIDTH//2+150, HEIGHT//2+150)
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
                        sleep_bar.unit += 30
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

                            sleep_bar.unit = 100 
                            satiety_bar.unit = 100
                            happiness_bar.unit = 100
                            knowledge_bar.unit = 0 
                            course_counter = 1
                            game_time_sec = 0
                            game_time_min = 0
                            gaming = False
                            background = mainScreen
                            background_rect = mainScreen_rect
                            flag_buttons = 0
                            S1 = Student()
                            A1.restart()
                            A2.restart()
                            pygame.display.flip()
                            pygame.mixer.music.unpause()
                            continue
                            
                    else:
                        knowledge_bar.unit += KBTU_knoweldge_change
                    if sleep_bar.unit>=KBTU_sleep_change:
                        sleep_bar.unit += KBTU_sleep_change
                    if satiety_bar.unit>=KBTU_satiety_change:
                        satiety_bar.unit += KBTU_satiety_change
                    if happiness_bar.unit>=KBTU_happiness_change:
                        happiness_bar.unit += KBTU_happiness_change 
                
                kbtu_sound.play()
                pygame.mixer.music.pause()
                screen.blit(kbtu_inside, kbtu_inside_rect)
                pygame.display.flip()
            
                S1.rect.center = (WIDTH//2+150, HEIGHT//2-100)
                time.sleep(2)
                game_time_sec -= 2
                pygame.mixer.music.pause()    
                confirmation = None
            elif confirmation == False:
                confirmation = None
                S1.rect.center = (WIDTH//2+150, HEIGHT//2-100)
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
        screen.blit(unpbplay_small, unpbplay_small_rect)
        screen.blit(unpbexit_small, unpbexit_small_rect)
        screen.blit(unpbinfo_small, unpbinfo_small_rect)   

    pygame.display.flip() 
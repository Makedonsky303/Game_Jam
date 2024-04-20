import pygame
pygame.init()

def draw_all_game(surface, imageBar, imageBar_rect,kbtu_outside,kbtu_outside_rect,dormitory_outside,dormitory_outside_rect,
                  cinema_outside,cinema_outside_rect,cafe_outside,cafe_outside_rect,pb_no_small,pb_no_small_rect,
                  knowledge,knowledge_position_rect,sleep,sleep_position_rect,satiety,satiety_position_rect,happiness,happiness_position_rect,knowledge_points, knowledge_points_rect, 
                  sleep_points, sleep_points_rect, satiety_points, satiety_points_rect, happiness_points, happiness_points_rect, course_counter_text, course_counter_text_rect, game_time_text, game_time_rect, 
                  knowledge_bar,  sleep_bar, satiety_bar, happiness_bar,
                  unpb_yes_small, unpb_yes_small_rect, unpb_no_small, unpb_no_small_rect):
    pygame.draw.rect(surface, (255, 255, 255), (250+200,70, 350, 200))
    surface.blit(imageBar, imageBar_rect)
    pygame.draw.rect(surface, (152, 136, 131), (250+200,455, 350, 100))
    pygame.draw.rect(surface, (152, 136, 131), (250+200,170, 350, 100))
    surface.blit(kbtu_outside, kbtu_outside_rect)
    surface.blit(dormitory_outside, dormitory_outside_rect)
    surface.blit(cinema_outside, cinema_outside_rect)
    surface.blit(cafe_outside, cafe_outside_rect)

    surface.blit(pb_no_small, pb_no_small_rect)

    knowledge_bar.draw(surface)
    sleep_bar.draw(surface)
    satiety_bar.draw(surface)
    happiness_bar.draw(surface)

    surface.blit(knowledge, knowledge_position_rect)
    surface.blit(sleep, sleep_position_rect)
    surface.blit(satiety, satiety_position_rect)
    surface.blit(happiness, happiness_position_rect)

    surface.blit(knowledge_points, knowledge_points_rect)
    surface.blit(sleep_points, sleep_points_rect)
    surface.blit(satiety_points, satiety_points_rect)
    surface.blit(happiness_points, happiness_points_rect)
    surface.blit(knowledge, knowledge_position_rect)
    surface.blit(sleep, sleep_position_rect)
    surface.blit(satiety, satiety_position_rect)
    surface.blit(happiness, happiness_position_rect)
    surface.blit(course_counter_text, course_counter_text_rect)
    surface.blit(game_time_text, game_time_rect)

    surface.blit(unpb_yes_small, unpb_yes_small_rect)
    surface.blit(unpb_no_small, unpb_no_small_rect)

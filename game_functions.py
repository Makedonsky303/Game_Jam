import pygame
pygame.init()

def draw_all_game(surface, imageBar, imageBar_rect,kbtu_outside,kbtu_outside_rect,dormitory_outside,dormitory_outside_rect,
                  cinema_outside,cinema_outside_rect,cafe_outside,cafe_outside_rect,pb_no_small,pb_no_small_rect,
                  knowledge,knowledge_position_rect,sleep,sleep_position_rect,satiety,satiety_position_rect,happiness,happiness_position_rect):
    surface.blit(imageBar, imageBar_rect)
    surface.blit(kbtu_outside, kbtu_outside_rect)
    surface.blit(dormitory_outside, dormitory_outside_rect)
    surface.blit(cinema_outside, cinema_outside_rect)
    surface.blit(cafe_outside, cafe_outside_rect)

    surface.blit(pb_no_small, pb_no_small_rect)

    surface.blit(knowledge, knowledge_position_rect)
    surface.blit(sleep, sleep_position_rect)
    surface.blit(satiety, satiety_position_rect)
    surface.blit(happiness, happiness_position_rect)
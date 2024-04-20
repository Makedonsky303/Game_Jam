import pygame
from settings import *
pygame.init()

#student sprites
face = pygame.image.load("student/face-to-screen.png")
face_small = pygame.transform.scale(face,(40, 40))
ass = pygame.image.load("student/ass-to-screen.png")
ass_small = pygame.transform.scale(ass,(40, 40))
right = pygame.image.load("student/right-dir-walk.png")
right_small = pygame.transform.scale(right,(40, 40))
left = pygame.image.load("student/left-dir-walk.png")
left_small = pygame.transform.scale(left,(40, 40))

class Student(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = face_small
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2 + 150, HEIGHT//2)
        self.direction = "down"

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left >= 0 and self.rect.right <= WIDTH:
          if (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]) and self.rect.left > 5 and ((self.rect.left  > CHARACTERISTICS_BAR_WIDTH + 5) or (self.rect.top > CHARACTERISTICS_BAR_HEIGHT + 20 + 5)):
              self.direction = "right"
              self.rect.move_ip(-5, 0)
          if (pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]) and self.rect.right < WIDTH - 5:
              self.direction = "left"
              self.rect.move_ip(5, 0)
        if self.rect.top >= 0 and self.rect.bottom <= HEIGHT:
          if (pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]) and self.rect.top > 5 and ((self.rect.left  > CHARACTERISTICS_BAR_WIDTH + 5) or (self.rect.top > CHARACTERISTICS_BAR_HEIGHT + 20 + 5)):
              self.direction = "up"
              self.rect.move_ip(0, -5)
          if (pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]) and self.rect.bottom < HEIGHT - 5:
              self.direction = "down"
              self.rect.move_ip(0, 5)  

    def draw(self, surface):
        if self.direction == "up":
            self.image = ass_small
            #rotated_image = self.image
        elif self.direction == "down":
            self.image = face_small
            #rotated_image = pygame.transform.rotate(self.image, 180)
        elif self.direction == "right":
            self.image = left_small
            #rotated_image = pygame.transform.rotate(self.image, 90)
        elif self.direction == "left":
            self.image = right_small
            #rotated_image = pygame.transform.rotate(self.image, -90)
        surface.blit(self.image, self.rect)
        #surface.blit(self.image, self.rect)
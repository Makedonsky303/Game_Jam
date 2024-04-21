import pygame
from settings import *
pygame.init()

student_size = 40
student_speed = 5

#student sprites
face = pygame.image.load("student/face-to-screen.png")
face_small = pygame.transform.scale(face,(student_size, student_size))
face_left = pygame.image.load("student/face-to-screen-left-leg.png")
face_left_small = pygame.transform.scale(face_left,(student_size, student_size))
face_right = pygame.image.load("student/face-to-screen-right-leg.png")
face_right_small = pygame.transform.scale(face_right,(student_size, student_size))

ass = pygame.image.load("student/ass-to-screen.png")
ass_small = pygame.transform.scale(ass,(student_size, student_size))
ass_left = pygame.image.load("student/ass-to-screen-left-leg.png")
ass_left_small = pygame.transform.scale(ass_left,(student_size, student_size))
ass_right = pygame.image.load("student/ass-to-screen-right-leg.png")
ass_right_small = pygame.transform.scale(ass_right,(student_size, student_size))

right_move = pygame.image.load("student/right-dir-walk.png")
right_move_small = pygame.transform.scale(right_move,(student_size, student_size))
right_stand = pygame.image.load("student/right-dir-stand.png")
right_stand_small = pygame.transform.scale(right_stand,(student_size, student_size))

left_move = pygame.image.load("student/left-dir-walk.png")
left_move_small = pygame.transform.scale(left_move,(student_size, student_size))
left_stand = pygame.image.load("student/left-dir-stand.png")
left_stand_small = pygame.transform.scale(left_stand,(student_size, student_size))

class Student(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = face_small
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2 + 150, HEIGHT//2-100)
        self.direction = "down"

        # изменение кадра
        self.count = 0

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left >= 0 and self.rect.right <= WIDTH:
          if (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]) and self.rect.left > 5 and ((self.rect.left  > CHARACTERISTICS_BAR_WIDTH + 5) or (self.rect.top > CHARACTERISTICS_BAR_HEIGHT + 20 + 5)):
              self.direction = "right"
              self.rect.move_ip(-student_speed, 0)
              self.count+=1
              if self.count>3:
                  self.count = 0   
        if (pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]) and self.rect.right < WIDTH - 5:
            self.direction = "left"
            self.rect.move_ip(student_speed, 0)
            self.count+=1
            if self.count>3:
                self.count = 0
        if self.rect.top >= 0 and self.rect.bottom <= HEIGHT:
          if (pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]) and self.rect.top > 5 and ((self.rect.left  > CHARACTERISTICS_BAR_WIDTH + 5) or (self.rect.top > CHARACTERISTICS_BAR_HEIGHT + 20 + 5)):
              self.direction = "up"
              self.rect.move_ip(0, -student_speed)
              self.count+=1
              if self.count>3:
                  self.count = 0
          if (pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]) and self.rect.bottom < HEIGHT - 5:
              self.direction = "down"
              self.rect.move_ip(0, student_speed)
              self.count+=1
              if self.count>3:
                  self.count = 0  

    def draw(self, surface):
        if self.direction == "up":
            
            if self.count==0 or self.count == 1:
                self.image = ass_left_small
            else:
                self.image = ass_right_small  
            #rotated_image = self.image
        elif self.direction == "down":
            if self.count == 0 or self.count == 1:
                self.image = face_left_small
            else:
                self.image = face_right_small
            #rotated_image = pygame.transform.rotate(self.image, 180)
        elif self.direction == "right":
            if self.count == 0 or self.count == 1:
                self.image = left_stand_small
            else:
                self.image = left_move_small
            #rotated_image = pygame.transform.rotate(self.image, 90)
        elif self.direction == "left":
            if self.count == 0 or self.count == 1:
                self.image = right_stand_small
            else:
                self.image = right_move_small
            #rotated_image = pygame.transform.rotate(self.image, -90)
        surface.blit(self.image, self.rect)
        #surface.blit(self.image, self.rect)
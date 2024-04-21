import pygame
from random import randint
from settings import *
pygame.init()



class Auto(pygame.sprite.Sprite):
    def __init__(self,car_image,side,car_speed):
        super().__init__() 
        self.image = pygame.image.load(car_image)
        self.rect = self.image.get_rect()
        self.side = side
        self.car_speed = car_speed
        if side=="top":
            self.rect.center=(randint(WIDTH+100, WIDTH+car_speed*300),HEIGHT//2)
        elif side=="bottom":
            self.rect.center=(randint(WIDTH+100, WIDTH+car_speed*300),HEIGHT//2+40)
        
    def move(self):
        self.rect.move_ip(-self.car_speed,0)
        if (self.rect.left < -96):
            if self.side=="top":
                self.rect.center=(randint(WIDTH+100, WIDTH+self.car_speed*500),HEIGHT//2)
            elif self.side=="bottom":
                self.rect.center=(randint(WIDTH+100, WIDTH+self.car_speed*500),HEIGHT//2+40)
    def restart(self):
        if self.side=="top":
            self.rect.center=(randint(WIDTH+100, WIDTH+self.car_speed*500),HEIGHT//2)
        elif self.side=="bottom":
            self.rect.center=(randint(WIDTH+100, WIDTH+self.car_speed*500),HEIGHT//2+40)            
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
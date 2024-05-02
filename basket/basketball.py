import pygame
import random
from settings import *

pygame.init()

#constants
ball_radius = 15
gravity = 0.15
drag_strength = 0.03

white = (255,255,255)
black = (0,0,0)

#game window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Basketball game")
bg = pygame.transform.scale(pygame.image.load("bg.png"), (1500, 700))

#loading images
ball_image = pygame.transform.scale(pygame.image.load("ball_image.png"), (30,30))
ring_image = pygame.transform.scale(pygame.image.load("ring_image.png"), (150,150))

#ball settings
ball = pygame.Rect(WIDTH // 2, HEIGHT - 100, 30, 30) #position of the ball
ball_velocity = [0, 0] #initial

ring_x = random.randint(100, HEIGHT - 200) # initial position (random)
ring_y = 150
ring = pygame.Rect(ring_x, ring_y, 100, 10) # ring in the center with width 100 and height 10

#initial states of the game
dragging = False
drag_start_pos = None
score = 0

font = pygame.font.Font(None, 36)

#main loop
running = True
while running:
    screen.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ball.collidepoint(event.pos): #check if click is within ball bounds
                dragging = True
                drag_start_pos = event.pos #remember the starting position for drag
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                dx = event.pos[0] - drag_start_pos[0]
                dy = event.pos[1] - drag_start_pos[1]
                ball_velocity = [dx * drag_strength, dy * drag_strength]  #scale the launch velocity
                dragging = False

    #updating ball position with velocity and gravity
    ball_velocity[1] += gravity
    ball.x += int(ball_velocity[0])
    ball.y += int(ball_velocity[1])

    #boundaries
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_velocity[0] = -ball_velocity[0] #inverting horizontal velocity if it hits the boundaries
    if ball.top <= 0:
        ball_velocity[1] = -ball_velocity[1] #inverting vertical velocity if it hits the top boundary

    #reseting ball position if it goes off the bottom
    if ball.y > HEIGHT - 100:
        ball = pygame.Rect(WIDTH // 2, HEIGHT - 100, 30, 30) #reset ball position
        ball_velocity = [0, 0]

    #checking for scoring collision with the ring
    if ball.bottom >= ring.top and ball.bottom <= ring.top + ball_velocity[1] and ball.colliderect(ring):
        #scoring only if hitting the top edge of the ring
        score += 1
        #reseting the ball position and velocity
        ball = pygame.Rect(WIDTH // 2, HEIGHT, 30, 30)
        ball_velocity = [0, 0]
        #randomizing the ring position
        ring.x = random.randint(100, HEIGHT - 200)

    screen.blit(ring_image, (ring.x - 25, ring.y - 75)) #centering the ring image around the rect
    screen.blit(ball_image, ball.topleft)

    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
    

import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 600
wn =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
run = True

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.12, 0.12

#paddle
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_height/2)
right_paddle_vel = left_paddle_vel = 0 
paddle_vel_constant = 0.3


#main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -paddle_vel_constant
            if i.key == pygame.K_DOWN:
                right_paddle_vel = paddle_vel_constant
            if i.key == pygame.K_w:
                left_paddle_vel = -paddle_vel_constant
            if i.key == pygame.K_s:
                left_paddle_vel = paddle_vel_constant
        if i.type == pygame.KEYUP:
            right_paddle_vel = 0 
            left_paddle_vel = 0 


    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 -radius
        ball_vel_x *= -1
        ball_vel_y *= -1
    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x, ball_vel_y = 0.12, 0.12

    #paddle collisions
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
            
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1



    #paddle movements
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0


    #movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    
    #OBJECTS
    pygame.draw.circle(wn, WHITE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, WHITE, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, WHITE, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update()

import pygame
import time
from player import Player
from platform_1 import Platforms
import random
from devil import Devil

pygame.init()
my_font = pygame.font.Font(None, 25)
pygame.display.set_caption("Devil Shooter")
size = (800, 400)
screen = pygame.display.set_mode(size)
run = True

clock = pygame.time.Clock()

bg = pygame.image.load("nature.jpg")
ship_top = screen.get_height() - bg.get_height()
ship_left = screen.get_width()/2 - bg.get_width()/2

screen_rect = screen.get_rect()

game_over = False

start_screen = pygame.image.load("start.jpg")
start_top = screen.get_height() - start_screen.get_height()
start_left = screen.get_width()/2 - start_screen.get_width()/2


speed = 0
        
while speed == 0: #changes speed of enemy depending on difficulty
    difficulty = input("Type 'E' for Easy mode, 'M' for Medium mode, and 'H' for Hard mode: ")
    if difficulty == 'E':
        speed = 2
    elif difficulty == 'M':
        speed = 3
    elif difficulty == 'H':
        speed = 4
    else: 
        print("Invalid input")

p = Player(300,50)
p1 = Platforms(100,300)
p2 = Platforms(500,300)
p3 = Platforms(300,200)
if random.randint(0,1) == 1:
    d = Devil(660, 50)
else:
    d = Devil(20, 50)
solid_ground_list = [p1,p2,p3]
jump_time = 0
score = 0
display_score = my_font.render("Score: " + str(score), True, (0, 0, 0))


start_time = time.time()
while run:# main run loop
    keys_pressed = pygame.key.get_pressed()
    p.gravity() # check gravity
    p.update(solid_ground_list)
    d.gravity()
    d.update(solid_ground_list)
    p.rect.clamp_ip(screen_rect)
    if jump_time > 0:
        p.jump()
        jump_time -= 1
    seconds = round(time.time() - start_time, 2)
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys_pressed[pygame.K_SPACE]:#resets jump length if player attempt to jump
            if jump_time <= 0:
                jump_time = 60
        if event.type == pygame.MOUSEBUTTONUP and not game_over:#determines mouse position when clicks mouse
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            mouse_position = (mouse_x, mouse_y)
            if d.rect.collidepoint(mouse_position): #reassigns devil position if he is clicked and adds score
                    if random.randint(0,1) == 1:
                        new_x = 660
                    else:
                        new_x = 20
                    new_y = 50
                    d.move(new_x, new_y)
                    score = score + 1
                    display_score = my_font.render("Score: " + str(score), True, (0, 0, 0))
        if d.rect.y > 300: #respawns devil if he falls off the map
                if random.randint(0,1) == 1:
                    new_x = 660
                else:
                    new_x = 20
                new_y = 50
                d.move(new_x, new_y)
        if d.rect.x < p.rect.x and random.randint(speed,4) == 4:#speed changes depending on difficulty. Moves right if player is right of him
            d.move_right()
        elif d.rect.x > p.rect.x and random.randint(speed,4) == 4: #speed changes depending on difficulty. Moves left if player is left of him
            d.move_left()
        if keys_pressed[pygame.K_d]:#player moves right if clicks d
            p.move_right()
        if keys_pressed[pygame.K_a]:#player moves left if clicks a
            p.move_left()
        if p.rect.y > 270 or d.rect.x == p.rect.x: #player loses if devil is on top of him or he falls into the void somehow
            game_over = True

    if not game_over: #displays all the classes and text during the game
        display_time = "Time elapsed: " + str(seconds) + "s"
        render_time = my_font.render(display_time, True, (0, 0, 0))
        screen.blit(bg, (ship_left,ship_top))

        screen.blit(p.image, p.rect)
        screen.blit(d.image, d.rect)
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        screen.blit(p3.image, p3.rect)
        screen.blit(render_time, (0,0))
        screen.blit(display_score, (0,50))
    
    if game_over: # game over screen
        screen.blit(start_screen, (start_left,start_top))
        screen.blit(display_score, (360,240))
        end_message = my_font.render("Game Over", True, (255, 0, 0))
        my_font = pygame.font.Font(None, 50)
        screen.blit(end_message, (300,200))



    pygame.display.update()

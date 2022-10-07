from sys import platlibdir
import pygame
import random
import math

pygame.init()

#drawing the board
dartboard = pygame.display.set_mode(size=(512, 512))
x , y = (dartboard.get_size())
# x and y store the screen width and height
selection_box_blue = pygame.Rect(0,0, (x/2), y)
selection_box_red = pygame.Rect((x/2),0, x, y)
pygame.draw.rect(dartboard, [255,0,0], selection_box_red)
pygame.draw.rect(dartboard, [0,0,255], selection_box_blue)
pygame.display.flip()

player_bet = 0
print("Place your bet on which color will win by clicking the color")
while player_bet == 0:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousecoordinate = pygame.mouse.get_pos()
            if selection_box_blue.collidepoint(mousecoordinate) == True:
                player_bet += 1
                print("You bet on blue winning - best hope they win!")
            elif selection_box_red.collidepoint(mousecoordinate) == True:
                player_bet += 2
                print("You bet on red winning - best hope they win!")

#making backboard
#defining the bounds of the dartboard - (0,0) is the top left, will never change
dartboardback = pygame.Rect(0,0,x,y)

#Setting up the darboard here
pygame.draw.rect(dartboard, [255, 228, 196], dartboardback)
pygame.draw.circle(dartboard, [139, 69, 19], ((x/2),(y/2)), (x/2))
pygame.draw.line(dartboard, [0,0,0], (x/2,0), (x/2,y))
pygame.draw.line(dartboard, [0,0,0], (0,y/2), (x,y/2))
pygame.display.flip()
pygame.time.wait(2000)

#Setting up dart players
#stop is 513 to allow darts to land on pixel 512 (i.e. the player somehow throws a dart on the edge of the dartboard)

blue_player_point = 0
red_player_point = 0
roundamount = 10
#allow for 10 rounds with both players - otherwise only one player plays per round
turnamount = roundamount*2
initturn = 0

for i in range(initturn, turnamount):
    if i in range(initturn, turnamount,2):
        rand_dart_pos = (dart_x_pos, dart_y_pos) = (random.randrange(0, 513), random.randrange(0, 513))
        dist_from_center = math.hypot((x/2) - dart_x_pos, (y/2) - dart_y_pos)
        is_in_circle = dist_from_center <= x/2
        if is_in_circle is True:
            print("Red's aim appears to be good (Hit)")
            red_player_point += 1            
            pygame.draw.circle(dartboard, [255,0,0], rand_dart_pos, 8)
            pygame.display.flip()
            pygame.time.wait(1000)
        if is_in_circle is False:
            print("We need to recalibrate Red's eyeballs (Miss)")
            pygame.draw.circle(dartboard, [200,0,0], rand_dart_pos, 8)
            pygame.display.flip()
            pygame.time.wait(1000)
    elif i in range(initturn + 1, turnamount +1,2):
        rand_dart_pos = (dart_x_pos, dart_y_pos) = (random.randrange(0, 513), random.randrange(0, 513))
        dist_from_center = math.hypot((x/2) - dart_x_pos, (y/2) - dart_y_pos)
        is_in_circle = dist_from_center <= x/2
        if is_in_circle is True:
            print("Blue's aim appears to be good (Hit)")
            blue_player_point += 1            
            pygame.draw.circle(dartboard, [0,0,255], rand_dart_pos, 8)
            pygame.display.flip()
            pygame.time.wait(1000)
        if is_in_circle is False:
            print("We need to recalibrate Blue's eyeballs (Miss)")
            pygame.draw.circle(dartboard, [0,0,200], rand_dart_pos, 8)
            pygame.display.flip()
            pygame.time.wait(1000)
print("Red points:",red_player_point,"| Blue points:", blue_player_point)
game_result = 0

if red_player_point == blue_player_point:
    print("The game ended in a tie")
elif red_player_point > blue_player_point:
    game_result += 2
    print("Red won the game")
    if game_result == player_bet:
        print("You have predicted correctly")
    elif game_result != player_bet:
        print("You have predicted incorrectly")
elif blue_player_point > red_player_point:
    game_result += 1
    print("Blue won the game")
    if game_result == player_bet:
        print("You have predicted correctly")
    elif game_result != player_bet:
        print("You have predicted incorrectly")
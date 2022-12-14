from hashlib import new
from unittest import skip
import pygame

pygame.init()
graphscreen = pygame.display.set_mode((512,512))
iters = {}
upper_limit = 20
max_so_far = 0
max_val = 0
scale = 5
#the upper_limit +1 is to make range() include 20, so it evaluates from 2-20 inclusively
for i in range(2,upper_limit +1):
    inputvalue = i
    count = 0
    font = pygame.font.Font(None, 24)
    while inputvalue !=1:
        if inputvalue%2 == 0:
            inputvalue = inputvalue/2
            count += 1
        elif inputvalue%2 != 0:
            inputvalue = (inputvalue*3) + 1
            count += 1
        elif inputvalue ==1:
            break
    iters[i] = count
    print("Dictionary of values, and the amount of times the loop ran for that value:", iters)
    coords = [(x*scale,y*scale) for x, y in iters.items()] # This defines tuple (x,y) as the dict pair (key,value) - i.e. converts dict of tuples into a list of tuple coordinates
    if coords.__len__() >= 2:
        pygame.draw.lines(graphscreen, [0,0,255], False, coords)
        new_graph = pygame.transform.flip(graphscreen, False, True)
        graphscreen.blit(new_graph, (0,0))
    if count >= max_so_far:
        max_so_far = count
        max_val = i
    msgsetup = str(max_so_far)
    msg = font.render("Highest amount of loops so far: "+msgsetup+" times", True, [0,0,255], None)
    graphscreen.blit(msg,(10,10)) #(10,10) is the offset for the text so it doesn't appear at the exact corner of the screen, for asthetic purposes
    pygame.display.flip()
    pygame.time.wait(1000)
    graphscreen.fill([0,0,0])
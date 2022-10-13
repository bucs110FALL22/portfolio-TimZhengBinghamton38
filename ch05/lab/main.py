from hashlib import new
from unittest import skip
import pygame

pygame.init()
graphscreen = pygame.display.set_mode((512,512))
font = pygame.font.Font(None, 24)
iters = {}
upper_limit = 20
max_so_far = 0
max_val = 0
#the upper_limit +1 is to make range() include 20, so it evaluates from 2-20 inclusively
for i in range(2,upper_limit +1):
    inputvalue = i
    count = 0
    print("Test Value:",inputvalue)
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
    coords = [(x,y) for x, y in iters.items()] # This defines tuple (x,y) as the dict pair (key,value) - i.e. converts dict of tuples into a list of tuple coordinates
    print(coords)
    print(type(coords))
    if count >= max_so_far:
        max_so_far = count
        max_val = i
print(max_val, max_so_far)


print(iters)

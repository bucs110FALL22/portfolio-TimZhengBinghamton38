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
    coords = []
    coords.append(iters.items())
    print(coords)
    if coords.__len__() >= 2:
        pygame.draw.lines(graphscreen, [255,0,255], False, coords)
        new_graph = pygame.transform.flip(graphscreen, False, True)
        graphscreen.blit(new_graph, (0,0))
    if count >= max_so_far:
        max_so_far = count
        max_val = i
    print(max_val, max_so_far)


print(iters)

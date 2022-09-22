import turtle #1. import modules
import random
import pygame
import math


#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

# inclusive of 1 - 100, excludes 101
simplemichelangelo = random.randrange(1, 101)
simpleleonardo = random.randrange(1, 101)

michelangelo.forward(simplemichelangelo)
leonardo.forward(simpleleonardo)

michelangelo.goto(-100, 20)
leonardo.goto(-100,-20)

# inclusive of 1 - 10, excludes 11
for _ in range(10):
  complexmichelangelo = random.randrange(1,11)
  complexleonardo = random.randrange(1, 11)
  michelangelo.forward(complexmichelangelo)
  leonardo.forward(complexleonardo)

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
# PART B - complete part B here
pygame.init()
pygamewindow = pygame.display.set_mode(size=(160, 160))
pygamewindow.fill([0,0,0])
goodcolor = (6, 118, 138, 1)
def labshapedraw(numsideshape):
  coords=[]
  num_sides = numsideshape
  side_length = 50
  offset = 70

  for i in range(num_sides):
    theta = ((2.0 * math.pi * i)/ num_sides)
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    y = float(y)
    x = float(x)
    coords.append((x,y))
  pygame.draw.polygon(pygamewindow, goodcolor , coords)
  pygame.display.flip()
  pygame.time.wait(1500)
  pygamewindow.fill((0,0,0))
  pygame.display.flip()
  pygame.time.wait(1000)

EQUILATERAL_TRIANGLE_SIDES = 3
SQUARE_SIDES = 4
HEXAGON_SIDES = 6
NONAGON_SIDES = 9
CIRCLE_SORT_OF_SIDES = 360

labshapedraw(EQUILATERAL_TRIANGLE_SIDES)
labshapedraw(SQUARE_SIDES)
labshapedraw(HEXAGON_SIDES)
labshapedraw(NONAGON_SIDES)
labshapedraw(CIRCLE_SORT_OF_SIDES)

window.exitonclick()

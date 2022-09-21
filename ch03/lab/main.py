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
pygamewindow = pygame.display.set_mode()



window.exitonclick()

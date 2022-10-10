import random
import turtle


screenturtle = turtle.Screen()

cointurtle = turtle.Turtle()
cointurtle.shape("turtle")
cointurtle.speed(0)

angle = 90
distance = 50



def isinscreen():
  turtlex = cointurtle.xcor()
  turtley = cointurtle.ycor()
  screenx_range = screenturtle.window_width()/2
  screeny_range = screenturtle.window_height()/2
  if abs(turtlex) > screenx_range or abs(turtley) > screeny_range:
    return False
  return True

while isinscreen() is True:
  coin = random.randrange(0,2)
  if coin == 0:
    cointurtle.left(angle)
    cointurtle.forward(distance)
  elif coin == 1:
    cointurtle.right(angle)
    cointurtle.forward(distance)
  print(cointurtle.pos())
else:
  exit()


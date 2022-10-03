import random
import turtle


screenturtle = turtle.Screen()

cointurtle = turtle.Turtle()
cointurtle.shape("turtle")

while True:
  coin = random.randrange(0,2)
  if coin == 0:
    cointurtle.left(90)
    cointurtle.forward(50)
  elif coin == 1:
    cointurtle.right(90)
    cointurtle.forward(50)
  print(cointurtle.pos())
screenturtle.exitonclick()

import turtle

wn = turtle.Screen()
a_turtle = turtle.Turtle()
a_turtle.shape("turtle")
a_turtle.color("purple")

square_sides = 4
# Draws a square
for i in range(square_sides):
    a_turtle.forward(50)
    a_turtle.left(90)

# Lifts pen up to change the pen color, moves 125 pxiels(?) then places pen down and starts to draw another square
a_turtle.up()
a_turtle.color("red")
a_turtle.forward(125)
a_turtle.down()

for i in range(square_sides):
    a_turtle.forward(50)
    a_turtle.left(90)

wn.exitonclick()
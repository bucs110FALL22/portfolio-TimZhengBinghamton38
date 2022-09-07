import turtle

wn = turtle.Screen()
a_turtle = turtle.Turtle()
num_sides = int(input("Please input number of sides: "))
a_turtle.shape("turtle")
a_turtle.color("purple")
angle = 360/num_sides

for num_sides in [num_sides]:
    a_turtle.forward(50)
    a_turtle.left(angle)

wn.exitonclick()
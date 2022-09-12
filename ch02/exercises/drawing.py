import turtle

window = turtle.Screen()

superturtlev2 = turtle.Turtle()
superturtlev2.color("red")

num_sides = int(input("Enter the number of sides: "))
angle = 360/num_sides
line_length = int(input("Enter the length of the sides: "))

for i in range(num_sides):
    superturtlev2.forward(line_length)
    superturtlev2.left(angle)

window.exitonclick()
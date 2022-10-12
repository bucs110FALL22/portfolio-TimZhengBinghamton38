import turtle

def drawEqShape(myturtle=None,num_sides = 0, side_length=0):
    angle = 360/num_sides
    for i in range(num_sides):
        myturtle.forward(side_length)
        myturtle.left(angle)

icanseething = turtle.Screen()

functionturtle = turtle.Turtle()
functionturtle.shape("turtle")
functionturtle.color("green")

input_sides = int(input("Enter the number of sides: "))
input_length = int(input("Enter the length of the sides: "))

drawEqShape(functionturtle, input_sides, input_length)

icanseething.exitonclick()

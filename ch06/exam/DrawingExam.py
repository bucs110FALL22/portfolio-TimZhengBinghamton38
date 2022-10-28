from atexit import register
import math
import numpy
import turtle


"""
This function converts a given polar coordinate to its cartesean form
args: radius, theta (a given polar coordinate (r,theta))
return: an (x,y) coordinate
"""
def polarcoords_to_cartcoords(radius = 0, theta = 0):
    x = radius*math.cos(theta)
    y = radius*math.sin(theta)
    return (x,y)

"""
This defines the r(theta) function
args = x,theta
return = the result of the given function
"""
def r_theta_function(x=1,theta=1):
    return numpy.sin(x*theta)

"""
This gives the amount of angles the r(theta) function will compute - lower values for resoultion = higher levels of accuracy
Also allows for setting the lower and upper bounds of calculation
args: lowerbound, upperbound, resolution
result: a list of angles for the r(theta) function to use in its computations
"""
def get_list_of_angles_for_polar_coords(lowerbound = 0,upperbound = math.pi, resolution = 0.01):
    return numpy.arange(lowerbound,upperbound,resolution)


"""
This simply creates a screen for the turtle to draw on

return: a screen
"""
def paper():
    paper = turtle.Screen()
    return paper

def main():
    draw_paper = paper()
    scale = 100
    petals = 5
    angle_list = get_list_of_angles_for_polar_coords()
    coords_list = []
    polar_turtle = turtle.Turtle()
    polar_turtle.hideturtle()
    if scale == 0:
        print("Did you really set the scale to 0? Stupid idea, it destroys the flower.")
        scale = 100
    if petals == 1:
        print("A one-petaled flower? Exotic.")
    if petals == 0:
        print("A flower with no petals... thats just grass.")
        draw_paper.bgcolor("green")
    for i in angle_list:
        radius = r_theta_function(petals*i)
        (x,y) = polarcoords_to_cartcoords(radius,i)
        coords_list.append((x*scale,y*scale))
    for i in coords_list:
        polar_turtle.goto(i)
    draw_paper.exitonclick()

main()
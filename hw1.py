import turtle
import math

# Create a turtle object
my_turtle = turtle.Turtle()

# Define a function to plot a point on the heart shape
def heart_point(t, theta):
    t.penup()
    x = 16 * math.sin(theta)**3
    y = 13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta)
    t.goto(10*x, 10*y)
    t.pendown()

# Plot points on the heart shape
for theta in range(0, 360, 5):
    heart_point(my_turtle, math.radians(theta))

# Hide the turtle and show the drawing
my_turtle.hideturtle()
turtle.done()
# Write your code here :-)

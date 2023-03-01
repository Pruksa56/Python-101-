import turtle
import math

Osten = turtle.Turtle()
Osten.shape('turtle')
Osten.color('Black', 'Pink')
#Osten.pencolor('Black')
Osten.speed(5)

def heart_point(t, theta):

    t.penup()
    x = 16 * math.sin(theta)**3
    y = 13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta)
    t.goto(10*x, 10*y)
    t.pendown()

# Plot points on the heart shape
Osten.begin_fill()
for theta in range(0, 360, 5):
    heart_point(Osten, math.radians(theta))

# Hide the turtle and show the drawing
Osten.end_fill()
#Osten.hideturtle()
turtle.done()

#credit equation from : ChatGPT
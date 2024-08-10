import turtle
import math

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")  # set the background color
tim = turtle.Turtle()
tim.penup()
tim.goto(15,-70)
tim.color("black")
tim.write('Loading...',font = ('Courier New',15,'normal'),align = 'center')

tim.speed("slow")  
tim.penup()   # Lift the pen to move without drawing
colors = ["black","dim gray","gray","dark gray","silver","light gray","gainsboro","white smoke","white","black"]

# Function to draw a dotted circle
def dotted_circle(radius, dot_radius, num_dots):
    angle = 360 / num_dots  # Angle between each dot
    for _ in range(num_dots):
        tim.goto(radius * math.cos(math.radians(angle * _)), radius * math.sin(math.radians(angle * _)))
        tim.dot(dot_radius, colors[_])  
        tim.penup()
        tim.color("white")
        tim.goto(0, 0)  # Move back to the center

# Parameters: radius of the circle, radius of each dot, number of dots
dotted_circle(radius=25, dot_radius=10, num_dots=10)
turtle.hideturtle() # Hide the turtle
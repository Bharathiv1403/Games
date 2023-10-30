import turtle as t

# Set up the Turtle screen
screen = t.Screen()
screen.bgcolor("white")

# Create a Turtle object for drawing
ben_10 = t.Turtle()
ben_10.speed(1)

# Define a function to draw Ben 10's face
def draw_ben_10_face():
    ben_10.penup()
    ben_10.goto(0, -100)
    ben_10.pendown()
    ben_10.begin_fill()
    ben_10.circle(100)
    ben_10.end_fill()

# Define a function to draw Ben 10's eyes
def draw_ben_10_eyes():
    ben_10.penup()
    ben_10.goto(-41, 30)
    ben_10.pendown()
    ben_10.begin_fill()
    ben_10.circle(25)
    ben_10.end_fill()

    ben_10.penup()
    ben_10.goto(40, 31)
    ben_10.pendown()
    ben_10.begin_fill()
    ben_10.circle(20)
    ben_10.end_fill()

# Define a function to draw Ben 10's logo
def draw_ben_10_logo():
    ben_10.penup()
    ben_10.goto(0, -10)
    ben_10.pendown()
    ben_10.begin_fill()
    ben_10.circle(10)
    ben_10.end_fill()

# Draw Ben 10's face, eyes, and logo
draw_ben_10_face()
draw_ben_10_eyes()
draw_ben_10_logo()

# Close the Turtle graphics window on click
screen.exitonclick()

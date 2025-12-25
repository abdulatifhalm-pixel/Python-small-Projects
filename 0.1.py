import turtle

t = turtle.Turtle()

# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

# Move to a new position
t.penup()
t.goto(150, 0)
t.pendown()

# Draw a circle
t.circle(50)

# Move again
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw a triangle
for i in range(3):
    t.forward(100)
    t.left(120)

turtle.done()

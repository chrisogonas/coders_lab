import turtle
import random

colors = 'red', 'green', 'yellow', 'orange'

screen = turtle.Screen()
screen.bgcolor('black')

pen = turtle.Turtle()
# pen.pencolor('yellow')
pen.pencolor(random.choice(colors))
pen.speed(0)
pen.width(5)

for x in range(360):
    pen.forward(x)
    pen.left(59)
    print(x)

turtle.mainloop()

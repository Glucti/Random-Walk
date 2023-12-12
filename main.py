from turtle import Screen, Turtle
import random

DEGREES = [180, 270, 90, 0]

screen = Screen()
screen.setup(1000, 1000)
screen.colormode(255)

# rand color generator
def rand_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

turtle = Turtle()
turtle.pensize(20)
turtle.speed(20)

for i in range(500):
    turtle.color(rand_color_generator())
    turtle.forward(35)
    turtle.setheading(random.choice(DEGREES))





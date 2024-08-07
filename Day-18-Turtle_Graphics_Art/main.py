from turtle import Turtle, Screen
import random

timmy = Turtle()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = (r, g, b)
    return color













screen = Screen()
screen.exitonclick()
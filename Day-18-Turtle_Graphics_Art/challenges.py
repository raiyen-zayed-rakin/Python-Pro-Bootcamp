import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")


# # no.1
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for _ in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     timmy.color(random.choice(colours))
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)
turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = (r, g, b)
    return color


# direction = [0, 90, 180, 270]
# timmy.pensize(10)
timmy.speed(20)
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.setheading(random.choice(direction))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(20)



screen = Screen()
screen.exitonclick()

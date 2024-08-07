import random
import turtle
from turtle import Turtle, Screen
import colorgram

# color extraction
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 24)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

turtle.colormode(255)
tim = Turtle()
tim.speed(20)
color_list = [(234, 239, 235), (187, 163, 127), (238, 234, 236), (125, 78, 59), (153, 162, 176), (69, 94, 137), (47, 44, 41), (149, 183, 168), (227, 207, 134), (190, 141, 146), (208, 163, 18), (88, 128, 174), (40, 43, 50), (41, 44, 42), (47, 43, 46), (190, 110, 69), (94, 98, 96), (42, 61, 101), (83, 80, 83), (180, 192, 206), (89, 56, 43), (76, 63, 49)]

tim.penup()
tim.hideturtle()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


# tim.penup()
# tim.backward(250)
# tim.right(90)
# tim.forward(250)
# tim.left(90)
# for _ in range(10):
#     tim.pendown()
#     tim.dot(20, random.choice(color_list))
#     tim.penup()
#     tim.forward(50)

screen = Screen()
screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
starting_positions = [(-20, 0), (0, 0), (20, 0)]

for position in starting_positions:
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.goto(position)




















screen.exitonclick()

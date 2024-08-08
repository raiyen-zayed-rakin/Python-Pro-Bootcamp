import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(15)


def turn_right():
    tim.right(15)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.title("Welcome to fuck up")
screen.listen()
screen.onkeypress(fun=move_forward, key="Up")
screen.onkeypress(fun=move_backward, key="Down")
screen.onkeypress(fun=turn_left, key="Left")
screen.onkeypress(fun=turn_right, key="Right")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
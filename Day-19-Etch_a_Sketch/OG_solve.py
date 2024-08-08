from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forwards, key="Up")
screen.onkey(fun=move_backwards, key="Down")
screen.onkey(fun=turn_left, key="Left")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=clear, key="c")

screen.exitonclick()

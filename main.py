from turtle import Turtle, Screen

shad = Turtle()
screen = Screen()


def move_forward():
    shad.forward(10)


def move_backward():
    shad.backward(10)


def turn_left():
    shad.left(15)


def turn_right():
    shad.right(15)


def clear():
    shad.clear()
    shad.penup()
    shad.home()
    shad.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

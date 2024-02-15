import turtle
from turtle import Turtle, Screen

p = Turtle()
s = Screen()


def move_forward():
    p.forward(50)


def move_backward():
    p.forward(-50)


def turn_left():
    p.left(10)


def turn_right():
    p.right(10)


s.listen()
s.onkey(move_forward, "w")
s.onkey(move_backward, "s")
s.onkey(turn_left, "a")
s.onkey(turn_right, "d")
s.onkey(p.clear, "c")
s.textinput(title="Hello",prompt='Hello bro')
s.exitonclick()

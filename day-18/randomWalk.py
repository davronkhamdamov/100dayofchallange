from turtle import Turtle, Screen, colormode
import random

s = Screen()
p = Turtle()
colormode(255)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# directors = [0, 90, 180, 270]
p.speed(0)
# p.pensize(10)
#
# for _ in range(100):
#     p.color(randomColor())
#     p.forward(30)
#     p.setheading(random.choice(directors))
#
for _ in range(36):
    p.circle(100)
    p.color(randomColor())
    p.setheading(p.heading()+10)


s.exitonclick()

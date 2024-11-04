from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
t.speed(50)
s.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_graph)


draw_spirograph(5)

s.exitonclick()

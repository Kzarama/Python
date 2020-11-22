import turtle
from time import sleep

pen = turtle.Turtle()
pen.setheading(90)
pen.color('brown')
pen.pensize(2)
pen.speed(9)


def draw_branch(len):
    if len > 5:
        pen.forward(len)
        pen.right(25)
        draw_branch(len - 5)
        pen.left(50)
        draw_branch(len - 5)
        pen.right(25)
        pen.backward(len)


draw_branch(40)
sleep(10)

import turtle
from time import sleep

pen = turtle.Turtle()


def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def heart():
    pen.speed(1)
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    pen.speed(0)
    curve()
    pen.left(120)
    curve()
    pen.speed(1)
    pen.forward(112)
    pen.end_fill()


def txt():
    pen.up()
    pen.setpos(-18, 85)
    pen.down()
    pen.color('lightgreen')
    pen.write("Sofi", font=(
        "Verdana", 12, "bold"))
    pen.ht()


sleep(2)
heart()
txt()
sleep(5)
pen.ht()

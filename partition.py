# partition.py
from turtle import Turtle, Screen


class Partition:
    def __init__(self):


        self.tim = Turtle()
        self.tim.color("white")
        self.tim.shape("square")
        #self.screen.tracer(0)
        self.tim.shapesize(1, 0.3)
        self.tim.pensize(5)
        self.tim.penup()
        self.tim.hideturtle()
        self.tim.goto(0, 300)
        self.tim.setheading(270)
        self.tim.speed("fastest")

        self.draw_partition()

    def draw_partition(self):
        for _ in range(30):
            self.tim.pendown()
            self.tim.forward(10)
            self.tim.penup()
            self.tim.forward(10)
        #self.screen.update()










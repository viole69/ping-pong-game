from turtle import Turtle,Screen
class Bats(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(3.5,1)
        self.penup()
        self.goto(position)








    def move_bat1_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_bat1_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

    def move_bat2_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_bat2_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)















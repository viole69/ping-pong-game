# main.py
from turtle import Turtle,Screen
from partition import Partition
from bats import Bats
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
partition_instance = Partition()
scoreboard=Scoreboard()

r_bat=Bats((280,0))
l_bat=Bats((-280,0))
ball_instance=Ball()


screen.listen()
screen.onkey(l_bat.move_bat1_up, "w")      # Move bat 1 up with 'W'
screen.onkey(l_bat.move_bat1_down, "s")    # Move bat 1 down with 'S'

screen.onkey(r_bat.move_bat2_up, "Up")     # Move bat 2 up with the Up arrow key
screen.onkey(r_bat.move_bat2_down, "Down")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball_instance.move()

    if ball_instance.ycor()>280 or ball_instance.ycor()<-280 :
        ball_instance.bounce_y()

    if ball_instance.distance(r_bat)<50 and ball_instance.xcor()>260:
        ball_instance.bounce_x()
    elif ball_instance.distance(l_bat) < 50 and ball_instance.xcor() > -270:
        ball_instance.bounce_x()

    if ball_instance.xcor()>280:
        ball_instance.reset_position()
        scoreboard.l_point()

    if ball_instance.xcor()<-280:
        ball_instance.reset_position()
        scoreboard.r_point()


screen.exitonclick()

















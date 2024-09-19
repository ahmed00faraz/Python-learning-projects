import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
turtle.register_shape("images/old_man.gif")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/old_man.gif")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)


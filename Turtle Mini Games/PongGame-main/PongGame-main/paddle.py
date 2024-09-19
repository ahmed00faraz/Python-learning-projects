from turtle import Turtle

SPEED = 30


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x, y=y)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + SPEED)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - SPEED)

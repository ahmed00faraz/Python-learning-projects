from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=650)
screen.title("PingPong")
screen.tracer(0)

r_Paddle = Paddle(350, 0)
l_Paddle = Paddle(-350, 0)
screen.update()

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(r_Paddle.go_up, "Up")
screen.onkeypress(r_Paddle.go_down, "Down")
screen.onkeypress(l_Paddle.go_up, "w")
screen.onkeypress(l_Paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.SPEED)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < - 300:
        ball.y_bounce()

    # collision with paddle
    if ball.distance(r_Paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()
    if ball.distance(l_Paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()

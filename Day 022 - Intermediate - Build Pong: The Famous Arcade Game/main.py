from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

R_STARTING_POSITIONS = (350, 0)
L_STARTING_POSITIONS = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(R_STARTING_POSITIONS)
l_paddle = Paddle(L_STARTING_POSITIONS)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball_heading = 45
move_speed = 0.1
game_is_on = True
while game_is_on:
    ball.ball_move(ball_heading)
    screen.update()
    time.sleep(move_speed)

    # Detect collision top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball_heading = 360 - ball.heading()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) \
            or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball_heading = ball.heading() - 90
        move_speed *= 0.8

    # Detect ball out of bound
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            ball_heading = 225
            score.l_point()
        else:
            ball_heading = 45
            score.r_point()
        move_speed = 0.1
        ball.ball_reset()

screen.exitonclick()

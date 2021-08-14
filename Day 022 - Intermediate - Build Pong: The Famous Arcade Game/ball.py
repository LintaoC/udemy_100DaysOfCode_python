from turtle import Turtle

STARTING_POSITION = (0, 0)
MOVE_DISTANCE = 10


class Ball:
    def __init__(self):
        self.ball = Turtle(shape="circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(STARTING_POSITION)

    def ball_move (self):
        self.ball.setheading(36.87)
        self.ball.forward(MOVE_DISTANCE)




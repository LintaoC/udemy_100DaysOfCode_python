import turtle as t

STARTING_POSITION = (0, 0)
MOVE_DISTANCE = 10


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)

    def ball_move(self, heading):
        self.setheading(heading)
        self.forward(MOVE_DISTANCE)

    def ball_reset(self):
        self.goto(0, 0)

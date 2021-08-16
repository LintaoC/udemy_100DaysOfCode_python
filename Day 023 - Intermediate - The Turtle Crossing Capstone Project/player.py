import turtle as t
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.setheading(90)
        self.penup()
        self.goto_bottom()

    def goto_bottom(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

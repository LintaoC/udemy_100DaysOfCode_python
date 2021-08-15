import turtle as t

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 240:
            print(self.ycor())
            new_y = self.ycor() + 20
            self.goto(self.position[0], new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.position[0], new_y)

    def reset_position(self):
        pass

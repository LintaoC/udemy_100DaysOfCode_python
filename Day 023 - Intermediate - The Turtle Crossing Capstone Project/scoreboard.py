import turtle as t

FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-270, 250)


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.goto(SCORE_POSITION)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=FONT)

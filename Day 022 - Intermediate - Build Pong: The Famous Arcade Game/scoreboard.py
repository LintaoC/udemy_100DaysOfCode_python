import turtle as t

ALIGNMENT = "CENTER"
FONT = ("Courier", 60, "normal")


class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("White")

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
import turtle as t

ALIGNMENT = "CENTER"
FONT = ("Courier", 16, "normal")


class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("White")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score= {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()



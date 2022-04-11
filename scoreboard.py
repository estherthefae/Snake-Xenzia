from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-50, 280)
        self.write_score()

    def update_score_normal(self):
        self.score += 1

    def update_score_big(self):
        self.score += 5

    def write_score(self):
        self.write(f"Score: {self.score}", font="Courier")

    def end_game(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER\nFinal Score: {self.score}", align="center", font=("Courier", 25, "bold"))

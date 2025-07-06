from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 15, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,225)
        self.update_score(self.score)
    def update_score(self, score):
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_score(self.score)
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", align=ALIGNMENT, font=FONT)
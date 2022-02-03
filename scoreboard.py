from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p_one_score = 0
        self.p_two_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
       self.clear()
       self.goto(-100, 200)
       self.write(self.p_two_score, align="center", font=("Courier", 80, "normal"))
       self.goto(100, 200)
       self.write(self.p_one_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.p_two_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.p_one_score += 1
        self.update_scoreboard()
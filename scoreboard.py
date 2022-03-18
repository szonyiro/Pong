from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(self.left_score, align="center", font=("Carrier", 30, "normal"))
        self.write(self.right_score, align="center", font=("Carrier", 30, "normal"))

    def update_left_scoreboard(self):
        self.write(self.left_score, align="center", font=("Carrier", 30, "normal"))

    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_left_scoreboard()

    def update_right_scoreboard(self):
        self.write(self.right_score, align="center", font=("Carrier", 30, "normal"))

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_right_scoreboard()

    def middle_line(self):
        self.color("white")
        self.hideturtle()
        self.goto(0, 300)

from turtle import Turtle


class Board(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.pendown()

    def border(self):
        self.pensize(10)
        self.forward(800)

    def middle(self):
        self.setheading(270)
        for i in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()


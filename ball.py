from turtle import Turtle
import random
random_coordinates_x = [6, 7, 8, -6, -7, -8]
random_y = [-2.5, 1.2, 1.4]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.x_move = 8
        self.y_move = 3
        self.move_speed = 0.04

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= - 1

    def bounce_x(self):
        self.x_move *= - 1
        self.y_move += random.choice(random_y)
        self.move_speed *= 0.95

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.035
        self.bounce_x()
        self.bounce_y()
        self.x_move = random.choice(random_coordinates_x)
        self.y_move = random.choice(random_coordinates_x) - 3
        self.move()

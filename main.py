import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from board import Board

screen = Screen()
screen.setup(width=800, height=605, startx=283, starty=84)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0, 0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
left_score = Scoreboard((-175, 230))
right_score = Scoreboard((175, 230))
top_border = Board((-400, 292)).border()
bottom_border = Board((-400, -297)).border()
middle = Board((0, 295)).middle()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 350:
        left_score.increase_left_score()
        ball.reset()

    if ball.xcor() < -350:
        right_score.increase_right_score()
        ball.reset()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    if ball.distance(right_paddle) < 80 and ball.xcor() > 320 or \
            ball.distance(left_paddle) < 80 and ball.xcor() < - 320:
        ball.bounce_x()

screen.exitonclick()

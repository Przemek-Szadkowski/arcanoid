from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
ball = Ball()


def combine_two_functions_with_left_key():
    paddle.move_left()
    ball.stick_to_paddle_move_left()


def combine_two_functions_with_right_key():
    paddle.move_right()
    ball.stick_to_paddle_move_right()


screen.listen()
screen.onkey(combine_two_functions_with_left_key, "Left")
screen.onkey(combine_two_functions_with_right_key, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
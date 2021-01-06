from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import Block
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.colormode(255)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
blocks = []
x = -420
y = 290

# creating blocks

for _ in range (0,6):
    x = -420
    y -= 35
    for number in range(0, 11):
        x += 70
        block = Block()
        blocks.append(block)
        block.goto(x, y)

game_is_on = True

# combine onkey functions with left and right keys


def combine_two_functions_with_left_key():
    paddle.move_left()
    ball.stick_to_paddle_move_left()


def combine_two_functions_with_right_key():
    paddle.move_right()
    ball.stick_to_paddle_move_right()


screen.listen()
screen.onkey(combine_two_functions_with_left_key, "Left")
screen.onkey(combine_two_functions_with_right_key, "Right")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()

    if ball.ycor() > 380:
        ball.bounce_y()

    if ball.ycor() == -310 and paddle.distance(ball) <= 83:
        ball.paddle_bounce()

    for block in blocks:
        if block.distance(ball) < 30:
            ball.bounce_y()
            block.reset()
            block.goto(1000, 1000)

#     paddle bounce
#     press space to start
#     reset ball after > ycor() 400

screen.exitonclick()
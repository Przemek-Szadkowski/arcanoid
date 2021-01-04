from turtle import Turtle

MOVE_AMMOUNT = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.color("white")
        self.penup()
        self.goto(0, -330)

    def move_left(self):
        if self.xcor() > -325:
            self.backward(MOVE_AMMOUNT)

    def move_right(self):
        if self.xcor() < 325:
            self.forward(MOVE_AMMOUNT)
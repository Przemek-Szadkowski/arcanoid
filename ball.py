from turtle import Turtle

MOVE_AMMOUNT = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -300)

    def stick_to_paddle_move_left(self):
        if self.xcor() > -325 and self.ycor() == -310:
            self.backward(MOVE_AMMOUNT)

    def stick_to_paddle_move_right(self):
        if self.xcor() < 325 and self.ycor() == -310:
            self.forward(MOVE_AMMOUNT)
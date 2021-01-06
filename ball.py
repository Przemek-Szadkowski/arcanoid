from turtle import Turtle

MOVE_AMMOUNT = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 15
        self.y_move = 15
        self.goto(0, -310)

    def stick_to_paddle_move_left(self):
        if self.xcor() > -325 and self.ycor() == -310:
            self.backward(MOVE_AMMOUNT)

    def stick_to_paddle_move_right(self):
        if self.xcor() < 325 and self.ycor() == -310:
            self.forward(MOVE_AMMOUNT)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.y_move *= -1


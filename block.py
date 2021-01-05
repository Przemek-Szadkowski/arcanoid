from turtle import Turtle


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.create_block()

    def create_block(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
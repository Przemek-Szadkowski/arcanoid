from turtle import Turtle
import random

COLORS = [(255, 210, 0), (45, 29, 72), (0, 165, 113), (240, 66, 39)]


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.create_block()

    def create_block(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
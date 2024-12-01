from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("orange")
        self.apear()
        
    def apear(self):
        x_cord = randint(-380, 380)
        y_cord = randint(-380, 380)
        self.goto(x_cord, y_cord)

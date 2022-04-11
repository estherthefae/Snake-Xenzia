from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.normal_ball()

    def normal_ball(self):
        self.shapesize(stretch_len = 0.4, stretch_wid = 0.4)
        self.color("blue")
        self.speed("fastest")
        self.change_food_location()

    def change_food_location(self):
        xcor = randint(-280, 280)
        ycor = randint(-280, 280)
        self.goto(xcor, ycor)

    def big_ball(self):
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("red")
        self.speed("fastest")
        self.change_food_location()


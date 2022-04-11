from turtle import Turtle
import time


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

SPEED = 0.1


class Snake:
    def __init__(self):
        self.tims = []
        self.create_snake()
        self.head = self.tims[0]
        self.speed = SPEED

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_tim(i)

    def add_tim(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.tims.append(tim)

    def move(self):
        time.sleep(self.speed)
        for i in range(len(self.tims) - 1, 0, -1):
            x = self.tims[i - 1].xcor()
            y = self.tims[i - 1].ycor()
            self.tims[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        self.speed *= 0.9
        time.sleep(self.speed)
        self.add_tim(self.tims[-1].position())


    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

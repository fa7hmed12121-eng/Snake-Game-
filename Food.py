from turtle import Turtle
import random

class food(Turtle):
    #food body
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5,0.5)
        self.penup()
        self.move()

    #make it move
    def move(self):
        self.goto(random.randint(-350,350),random.randint(-230,230))
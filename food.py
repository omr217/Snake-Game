from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_coordinate = random.randint(-280,280)
        y_coordinate = random.randint(-280, 280)
        self.goto(x_coordinate, y_coordinate)



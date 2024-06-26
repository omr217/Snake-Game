from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
FORWARD = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for positions in POSITION:
            self.add_segment(positions)

    def add_segment(self , positions):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(positions)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(FORWARD)

    def turn_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)

    def turn_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def turn_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def turn_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-15, 0), (-30, 0)]
RIGHT=0
LEFT=180
UP=90
DOWN=270
class Snake:
    def __init__(self):
        self.segments=[]
        self.snake()
        self.head=self.segments[0]
    def snake(self):
        for position in STARTING_POSITIONS:
             self.add_segment(position)
    def add_segment(self,position):
        snake1 = Turtle(shape="square")
        snake1.shapesize(stretch_wid=0.75, stretch_len=0.75)
        snake1.color("white")
        snake1.penup()
        snake1.goto(position)
        self.segments.append(snake1)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for position in range(len(self.segments) - 1, 0, -1):
            x_cord = self.segments[position - 1].xcor()
            y_cord = self.segments[position - 1].ycor()
            self.segments[position].goto(x_cord, y_cord)
        self.segments[0].forward(15)
    def move_up(self):
        if self.segments[0]!=DOWN:
            self.segments[0].setheading(90)
            self.move()
    def move_right(self):
        if self.segments[0] != LEFT:
            self.segments[0].setheading(0)
            self.move()
    def move_left(self):
        if self.segments[0] != RIGHT:
            self.segments[0].setheading(180)
            self.move()
    def move_down(self):
        if self.segments[0] != UP:
            self.segments[0].setheading(270)
            self.move()



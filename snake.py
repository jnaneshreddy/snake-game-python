from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTENCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segemnts = []
        self.create_snake()
        self.head = self.segemnts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_segments = Turtle('square')
        new_segments.color('white')
        new_segments.penup()
        new_segments.goto(position)
        self.segemnts.append(new_segments)
    def extand(self):
        self.add_segment(self.segemnts[-1].position())

    def move(self):
        for seg_num in range(len(self.segemnts) - 1, 0, -1):
            new_x = self.segemnts[seg_num - 1].xcor()
            new_y = self.segemnts[seg_num - 1].ycor()
            self.segemnts[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTENCE)
        # self.segemnts[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




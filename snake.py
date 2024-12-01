from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_segment(self, position):
        snake = Turtle("square")
        snake.color("blue")
        snake.penup()
        self.segments.append(snake)
        snake.goto(position)

    def create_snake(self):
        for position in POSITION:
            self.create_segment(position)

    def get_rid_snake(self):
        for seg_num in self.segments:
            seg_num.teleport(1000, 1000)
        self.segments.clear()

    def extend(self):
        """Extend length of our snake """
        self.create_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_seg = self.segments[segment - 1].xcor()
            y_seg = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_seg, y_seg)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
            
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

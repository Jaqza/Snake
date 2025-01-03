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

    def snake_resets(self):
        for seg_num in self.segments:
            seg_num.teleport(1000, 1000)
        self.segments.clear()

    def create_snake(self):
        """ It builds 3 segments of a snake on a middle of the window"""
        for position in POSITION:
            self.create_segment(position)
        self.head = self.segments[0]

    def create_segment(self, position):
        """Inner funktion belonging to snake class , do not use it outside """
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def move(self):
        """ Funktion makes our snake to move."""
        for segment in range(len(self.segments) - 1, 0, -1):
            x_seg = self.segments[segment - 1].xcor()
            y_seg = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_seg, y_seg)
        self.segments[0].forward(20)

    def extend(self):
        """Extend length of our snake """
        self.create_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

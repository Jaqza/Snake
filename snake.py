import snake
from turtle import Turtle

class Snake:
    def __init__(self):
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.UP = 90
        self.LEFT = 180
        self.DOWN = 270
        self.RIGHT = 0


    def create_segment(self ,position):## cos z tymi pozycjami pokielbasilem
        self.snake = Turtle("square")
        self.snake.color("blue")
        self.snake.penup()
        self.segments.append(self.snake)
        self.snake.goto(position)

    def create_snake(self ):
        for position in self.position:
            self.create_segment(position)

        self.head = self.segments[0]
        self.head.color("cyan")

    def extend(self):
        """Extend lenght of our snake """
        self.create_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_seg = self.segments[segment - 1].xcor()
            y_seg = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_seg, y_seg)
        self.head.forward(20)
        
    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)
            
    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)
    
    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)
    
    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

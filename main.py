from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("gray")
screen.tracer(0)
screen.listen()

snake = Snake()

fruit = Food()

screen.update()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

is_game_on = True
scoreboard = Scoreboard()
while is_game_on:
    screen.update()
    time.sleep(0.10)
    snake.move()

    if fruit.distance(snake.segments[0]) < 15:
        fruit.apear()
        scoreboard.add_point()
        snake.extend()

    if snake.segments[0].xcor() > 380 or snake.segments[0].xcor() < -380 or snake.segments[0].ycor() > 380 or snake.segments[0].ycor() < -380:
        """I will add high scoare , it is the first time Iw will be working with files"""
        scoreboard.new_hi_score()
        snake.get_rid_snake()
        snake.create_snake()

    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            snake.get_rid_snake()
            snake.create_snake()







screen.exitonclick()
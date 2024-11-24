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
snake.create_snake()
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
    if fruit.distance(snake.head) < 15:
        fruit.apear()
        scoreboard.add_point()
        snake.extend()

    if snake.head.xcor() > 380 or snake.head.xcor() < -390 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            scoreboard.game_over()
            is_game_on = False







screen.exitonclick()
from turtle import Screen
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
scoreboard = Scoreboard()
screen.update()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.10)
    snake.move()

    if fruit.distance(snake.head) < 15:
        fruit.apear()
        scoreboard.add_point()
        snake.extend()

    if snake.head.xcor() > 395 or snake.head.xcor() < -395 or snake.head.ycor() > 395 or snake.head.ycor() < -395:
        scoreboard.new_hi_score()
        snake.snake_resets()
        snake.create_snake()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake.snake_resets()
            snake.create_snake()

screen.exitonclick()

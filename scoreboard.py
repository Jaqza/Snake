from turtle import Turtle
score = 0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.teleport(0, 370)
        self.add_point()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over !!!", False, "center", ("Courier", 18, "normal"))
    def add_point(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", False, "center", ("Courier", 18, "normal"))

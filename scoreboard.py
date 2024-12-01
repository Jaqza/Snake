from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("hi_score.txt", "r")as file:
            self.hi_score = int(file.read())
            file.close()
        self.penup()
        self.hideturtle()
        self.teleport(-370, 370)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} Hi-score:{self.hi_score}", False, "left", ("Courier", 18, "normal"))

    def add_point(self):
        self.score += 1
        self.update()

    def new_hi_score(self):
        self.clear()
        if self.score > self.hi_score:
            self.hi_score = self.score
            with open("hi_score.txt", "w") as file:
                file.write(f"{self.hi_score}")
        self.score = 0
        self.update()

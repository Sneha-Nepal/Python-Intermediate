from turtle import Turtle

FONT = ("Courier", 18, "bold")
LEVEL_POSITION = (-230, 260)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.display()

    def display(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(LEVEL_POSITION)
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def update(self):
        self.level += 1
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)

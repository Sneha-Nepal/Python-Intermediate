from turtle import Turtle

FONT = ("Courier", 18, "bold")
LEVEL_POSITION = (-230, 260)
TOP_POSITION = (0, 260)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()

    def display(self):
        self.clear()
        self.goto(LEVEL_POSITION)
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def update(self):
        self.level += 1
        self.display()

    def game_over(self):
        self.goto(TOP_POSITION)
        self.write(f"Game Over", align="center", font=FONT)

    def write_message(self, text):
        self.goto(TOP_POSITION)
        self.write(text, align="center", font=FONT)

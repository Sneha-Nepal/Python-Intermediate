from turtle import Turtle
FONT = ('Arial', 16 , 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        """Initializing Scoreboard class and inheriting Turtle class"""
        super().__init__()
        self.score = 0

        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 260)
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def update(self):
        """Update and display the score in the turtle Screen"""
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align="center", font=('Arial', 16 , 'bold'))

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game Over", align="center", font=('Arial', 16 , 'bold'))

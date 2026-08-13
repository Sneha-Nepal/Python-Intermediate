from turtle import Turtle
FONT = ('Arial', 16 , 'bold')
FILE_PATH = "snake_game/high_score.txt"

class Scoreboard(Turtle):

    def __init__(self):
        """Initializing Scoreboard class and inheriting Turtle class"""
        super().__init__()
        self.score = 0

        try:
            with open(FILE_PATH, "r") as file:
                self.high_score = int(file.read())
        except(FileNotFoundError, ValueError):
            self.high_score = 0

        self.penup()
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        """Update and display the score in the turtle Screen"""
        self.clear()
        self.goto(220, 260)
        self.write(f"Score : {self.score}", align="center", font=FONT)
        self.goto(-220, 260)
        self.write(f"High Score : {self.high_score}", align="center", font=FONT)

    def increment_score(self):
        """Increase the score"""
        self.score += 1
        self.update()

    def update_high_score(self):
        """Updates the high_score"""
        if self.high_score < self.score:
            self.high_score = self.score
        
        with open(FILE_PATH , "w") as file:
            file.write(str(self.high_score))

        self.score = 0
        self.update()

    def game_over(self):
        """Indicates that the game is over"""
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

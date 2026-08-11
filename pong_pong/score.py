from turtle import Turtle
FONT = ('Courier', 30 , 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        """Initializing Scoreboard class and inheriting Turtle class"""
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0

        self.penup()
        self.color("white")
        self.hideturtle()
        self.update()

    def draw_line(self):
        """Draws a dashed vertical line in the middle of the screen"""
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, -370)
        self.setheading(90)
        self.pensize(3)
        while self.ycor() < 370:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

    def update(self):
        """Update and display the score in the turtle Screen"""
        self.clear()
        self.draw_line()
        self.goto(150, 300)
        self.write(f"{self.score_1}", align="center", font=FONT)
        self.goto(-150, 300)
        self.write(f"{self.score_2}", align="center", font=FONT)       

    def update_1(self):
        """Updates the score for one of the paddle"""
        self.score_1 += 1
        self.update()

    def update_2(self):
        """Updates the score for one of the paddle"""
        self.score_2 += 1
        self.update()

    def game_over(self):
        """Indicates that the game is over"""
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

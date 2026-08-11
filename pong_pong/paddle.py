from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor):
        """Initializing the Paddle class. Ineriting from the Turtle class"""
        super().__init__()
        self.y_cor = 0
        self.x_cor = x_cor
        self.create()

    def create(self):
        """Creating paddles with specific shape and size. Also, initially setting them in their position"""
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(self.x_cor, self.y_cor)

    def up(self):
        """Moves the paddle to up direction as in increases the y-axis"""
        self.new_ycor = self.ycor() + 30
        self.goto(self.x_cor, self.new_ycor)

    def down(self):
        """Moves the paddle to down direction as in decreases the y-axis"""
        self.new_ycor = self.ycor() - 30
        self.goto(self.x_cor, self.new_ycor)
        
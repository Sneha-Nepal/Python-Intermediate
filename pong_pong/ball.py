from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        """Initializing the Paddle class. Ineriting from the Turtle class"""
        super().__init__()
        self.create_ball()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def create_ball(self):
        """Creates the ball and sets its color"""
        self.shape("circle")
        self.color("yellow")
        self.penup()

    def move(self):
        """Moves the ball in the y-axis and x-axis"""
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def change_direction_y(self):
        """Changes the direction as the ball hits the top or bottom of the screen"""
        self.y *= -1

    def change_direction_x(self):
        """Changes the direction as the ball hits one of the paddle and fastens the speed"""
        self.x *= -1
        self.move_speed *= 0.7

    def reset(self):
        """Resets the ball to the center of the screen and changes its direction"""
        self.goto(0,0)
        self.move_speed = 0.1
        self.change_direction_x()

